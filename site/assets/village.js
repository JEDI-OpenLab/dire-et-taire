/* Village animé : illustration du mécanisme d'une simulation du C4.
   Les règles sont volontairement simples et les réponses sont tirées au hasard :
   l'animation montre qui rencontre qui, où, et quand une sollicitation est posée,
   pas un résultat de l'expérience. */
(function(){
  const root = document.getElementById("village");
  if (!root) return;
  const svg = root.querySelector("svg");
  const NS = "http://www.w3.org/2000/svg";
  const W = 760, H = 470, N = 40, DAYS = 15, SLOTS = 3;
  const SLOT_NAMES = ["matin", "midi", "après-midi"];
  const GAZ_DAYS = [2, 5, 8, 11];

  const PLACES = [
    {id:"cafe", l:"Café", x:150, y:120},
    {id:"marche", l:"Marché", x:380, y:95},
    {id:"boul", l:"Boulangerie", x:610, y:120},
    {id:"salle", l:"Salle des fêtes", x:380, y:250}
  ];
  /* Dix maisons de quatre habitants, sur deux rangées en bas de la carte */
  const HOMES = [];
  for (let i = 0; i < 10; i++) HOMES.push({x: 80 + (i % 5) * 150, y: i < 5 ? 355 : 430});

  function mk(t, a, parent){const e=document.createElementNS(NS,t);for(const k in a)e.setAttribute(k,a[k]);if(parent)parent.appendChild(e);return e}
  function rng(seed){let s=seed>>>0;return function(){s=(s+0x6D2B79F5)>>>0;let t=s;t=Math.imul(t^(t>>>15),t|1);t^=t+Math.imul(t^(t>>>7),t|61);return((t^(t>>>14))>>>0)/4294967296}}
  function shuffle(a,r){for(let i=a.length-1;i>0;i--){const j=Math.floor(r()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}

  /* Population fixe : position déclarée de départ, maison, proches */
  const pop = (function(){
    const r = rng(42);
    const ag = [];
    for (let i = 0; i < N; i++) ag.push({i, home: Math.floor(i / 4), pos: r() * 2 - 1});
    ag.forEach(a => {
      const same = ag.filter(b => b.home === a.home && b.i !== a.i).map(b => b.i);
      const other = shuffle(ag.filter(b => b.home !== a.home).map(b => b.i), r).slice(0, 2);
      a.proches = same.concat(other);
    });
    return ag;
  })();

  /* Calcul de toute la simulation pour une configuration donnée */
  function simulate(ordo, gaz){
    const r = rng(7 + (ordo === "hom" ? 1000 : 0) + ["g0","geq","gp","gm"].indexOf(gaz) * 10);
    const informed = new Array(N).fill(false); informed[0] = true;
    const last = new Array(N).fill(null);
    const steps = [];
    let soll = 0, dits = 0, tus = 0;
    for (let d = 1; d <= DAYS; d++) {
      const gazToday = gaz !== "g0" && GAZ_DAYS.includes(d);
      if (gazToday && d === 2) informed.fill(true);
      for (let s = 0; s < SLOTS; s++) {
        let order = shuffle([...Array(N).keys()], r);
        const pub = [], priv = [], used = new Set();
        /* La moitié environ va dans une scène publique */
        let publicIds = order.filter(() => r() < 0.5);
        if (ordo === "hom") publicIds.sort((a, b) => pop[a].pos - pop[b].pos);
        let k = 0, p = 0;
        while (k < publicIds.length) {
          const size = 3 + Math.floor(r() * 3);
          const g = publicIds.slice(k, k + size);
          k += size;
          if (g.length < 3) break;
          pub.push({place: PLACES[p % PLACES.length], who: g});
          g.forEach(x => used.add(x));
          p++;
        }
        /* Les autres : tête-à-tête avec un proche, ou chez soi */
        order.forEach(a => {
          if (used.has(a)) return;
          const cands = pop[a].proches.filter(b => !used.has(b));
          if (cands.length && r() < 0.75) {
            let b = cands[Math.floor(r() * cands.length)];
            if (ordo === "hom") b = cands.slice().sort((x, y) => Math.abs(pop[x].pos - pop[a].pos) - Math.abs(pop[y].pos - pop[a].pos))[0];
            priv.push({who: [a, b]}); used.add(a); used.add(b);
          }
        });
        /* Circulation : le livre est évoqué dans une scène où quelqu'un le connaît */
        const scenes = pub.map(x => ({...x, kind: "pub"})).concat(priv.map(x => ({...x, kind: "priv"})));
        const events = [];
        scenes.forEach(sc => {
          const knows = sc.who.some(x => informed[x]);
          if (knows && r() < 0.6) sc.who.forEach(x => informed[x] = true);
          /* Sollicitation standardisée : une question ouverte, une réponse tirée au hasard */
          if (r() < 0.45) {
            const inf = sc.who.filter(x => informed[x]);
            if (inf.length) {
              const a = inf[Math.floor(r() * inf.length)];
              const dit = r() < 0.5;
              last[a] = dit ? "dit" : "tait";
              soll++; dit ? dits++ : tus++;
              events.push({a, dit, sc});
            }
          }
        });
        steps.push({d, s, scenes, events, gaz: gazToday, informed: informed.slice(), last: last.slice(), soll, dits, tus});
      }
    }
    return steps;
  }

  /* Décor */
  const gDecor = mk("g", {}, svg), gEdges = mk("g", {}, svg), gEvents = mk("g", {}, svg), gAgents = mk("g", {}, svg), gBanner = mk("g", {}, svg);
  PLACES.forEach(pl => {
    mk("circle", {cx: pl.x, cy: pl.y, r: 58, class: "box-v", "fill-opacity": .55}, gDecor);
    const t = mk("text", {x: pl.x, y: pl.y - 64, "text-anchor": "middle", class: "t-s muted"}, gDecor); t.textContent = pl.l;
  });
  HOMES.forEach((h, i) => {
    mk("rect", {x: h.x - 34, y: h.y - 26, width: 68, height: 52, rx: 6, class: "box"}, gDecor);
  });
  const tHomes = mk("text", {x: 20, y: 316, class: "t-s muted"}, gDecor); tHomes.textContent = "Maisons (tête-à-tête entre proches)";

  /* Agents */
  const agentEls = pop.map(a => {
    const g = mk("g", {class: "ag"}, gAgents);
    const c = mk("circle", {r: 7.5, "stroke-width": 1.6}, g);
    if (a.i === 0) { const t = mk("text", {y: 3.5, "text-anchor": "middle", class: "mono", "font-size": 9, "font-weight": 600}, g); t.textContent = "L"; }
    return {g, c};
  });

  function homeSpot(i){const h = HOMES[pop[i].home]; const k = i % 4; return {x: h.x - 24 + k * 16, y: h.y - 12}}

  const els = {
    play: root.querySelector("#v-play"), next: root.querySelector("#v-next"), day: root.querySelector("#v-day"),
    ordo: root.querySelectorAll("input[name=v-ordo]"), gaz: root.querySelector("#v-gaz"),
    out: {day: root.querySelector("#c-day"), inf: root.querySelector("#c-inf"), pub: root.querySelector("#c-pub"), priv: root.querySelector("#c-priv"), soll: root.querySelector("#c-soll"), dit: root.querySelector("#c-dit"), tait: root.querySelector("#c-tait")}
  };
  let steps = [], cur = 0, timer = null;

  function cfg(){return {ordo: [...els.ordo].find(x => x.checked).value, gaz: els.gaz.value}}
  function rebuild(keep){const c = cfg(); steps = simulate(c.ordo, c.gaz); if (!keep) cur = 0; render()}

  function render(){
    const st = steps[cur];
    const pos = new Array(N);
    gEdges.textContent = ""; gEvents.textContent = ""; gBanner.textContent = "";
    st.scenes.forEach(sc => {
      if (sc.kind === "pub") {
        sc.who.forEach((a, j) => {const ang = (j / sc.who.length) * Math.PI * 2 - Math.PI / 2; pos[a] = {x: sc.place.x + Math.cos(ang) * 30, y: sc.place.y + Math.sin(ang) * 30}});
      } else {
        const h = HOMES[pop[sc.who[0]].home];
        pos[sc.who[0]] = {x: h.x - 13, y: h.y + 12}; pos[sc.who[1]] = {x: h.x + 13, y: h.y + 12};
      }
      for (let i = 0; i < sc.who.length; i++) for (let j = i + 1; j < sc.who.length; j++) {
        const a = sc.who[i], b = sc.who[j];
        mk("line", {x1: pos[a].x, y1: pos[a].y, x2: pos[b].x, y2: pos[b].y, class: sc.kind === "pub" ? "edge-t" : "edge-v", "stroke-opacity": .55}, gEdges);
      }
    });
    pop.forEach(a => { if (!pos[a.i]) pos[a.i] = homeSpot(a.i); });
    agentEls.forEach((e, i) => {
      e.g.style.transform = `translate(${pos[i].x.toFixed(1)}px,${pos[i].y.toFixed(1)}px)`;
      const inf = st.informed[i], last = st.last[i];
      e.c.setAttribute("class", "");
      e.c.style.fill = last === "dit" ? "var(--amber)" : last === "tait" ? "var(--slate)" : inf ? "var(--teal-soft)" : "var(--surface)";
      e.c.style.stroke = i === 0 ? "var(--violet)" : inf ? "var(--teal)" : "var(--muted)";
      e.c.setAttribute("stroke-width", i === 0 ? 2.6 : 1.6);
      const txt = e.g.querySelector("text"); if (txt) txt.style.fill = last ? "var(--surface)" : "var(--ink)";
    });
    st.events.forEach(ev => {
      const p = pos[ev.a];
      mk("circle", {cx: p.x, cy: p.y, r: 13, fill: "none", "stroke-width": 2, style: `stroke:${ev.dit ? "var(--amber)" : "var(--slate)"}`, "stroke-dasharray": ev.dit ? "" : "3 2"}, gEvents);
    });
    if (st.gaz) {
      const g = mk("g", {transform: "translate(600,12)"}, gBanner);
      mk("rect", {width: 150, height: 26, rx: 5, class: "box-a"}, g);
      const t = mk("text", {x: 75, y: 17, "text-anchor": "middle", class: "t-s"}, g);
      t.textContent = "Gazette du jour " + ({geq: "(neutre)", gp: "(favorable)", gm: "(critique)"})[cfg().gaz];
    }
    const pubN = st.scenes.filter(s => s.kind === "pub").length, privN = st.scenes.length - pubN;
    els.out.day.textContent = `Journée ${st.d}, ${SLOT_NAMES[st.s]}`;
    els.out.inf.textContent = `${st.informed.filter(Boolean).length} / ${N}`;
    els.out.pub.textContent = pubN; els.out.priv.textContent = privN;
    els.out.soll.textContent = st.soll; els.out.dit.textContent = st.dits; els.out.tait.textContent = st.tus;
    els.day.value = st.d;
  }

  function step(){cur = (cur + 1) % steps.length; render()}
  function stop(){clearInterval(timer); timer = null; els.play.textContent = "Lancer"; els.play.setAttribute("aria-pressed", "false")}
  els.play.addEventListener("click", () => {
    if (timer) return stop();
    timer = setInterval(step, 1200); els.play.textContent = "Pause"; els.play.setAttribute("aria-pressed", "true");
  });
  els.next.addEventListener("click", () => {stop(); step()});
  els.day.addEventListener("input", () => {stop(); cur = (parseInt(els.day.value, 10) - 1) * SLOTS; render()});
  els.ordo.forEach(x => x.addEventListener("change", () => rebuild(true)));
  els.gaz.addEventListener("change", () => rebuild(true));
  rebuild(false);
  /* Les déplacements ne sont animés qu'après le premier rendu, et seulement si le lecteur l'accepte */
  const calm = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!calm) requestAnimationFrame(() => requestAnimationFrame(() => agentEls.forEach(e => e.g.style.transition = "transform .7s ease")));
})();
