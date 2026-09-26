/* ============================================================
   FIRST SPIN DJ BOOTCAMP — shared behavior + CONFIG
   Staff: set live links & endpoints here (one place, all pages).
   ============================================================ */
window.FIRST_SPIN_CONFIG = {
  // Parent 2027 interest list — approved Google Form.
  // Every "Join the 2027 Interest List" button opens this.
  interestFormUrl: "https://docs.google.com/forms/d/e/1FAIpQLSdrJJnw7UlveyVE3LE9332Fr0D1CDEhuYfOBKeybyquc-DRCg/viewform",

  // Donation URL — SpotFund (MixHer Inc. / First Spin). Powers "Donate to First Spin".
  donateUrl: "https://www.spotfund.com/story/0eca9210-2fdb-46e5-b0ac-4e155f853170",

  // Newsletter signup URL (email platform). Leave "" to use the on-page form fallback.
  newsletterUrl: "",

  // Generic form endpoint (Formspree/etc) for sponsor, venue, contact forms.
  formEndpoint: "",              // e.g. "https://formspree.io/f/XXXX"

  contactEmail: "FirstSpinDJBootcamp@gmail.com",

  // GA4 Measurement ID (G-XXXX) to auto-load analytics; events also push to dataLayer (GTM).
  ga4MeasurementId: ""
};

(function(){
  "use strict";
  document.documentElement.className = document.documentElement.className.replace("no-js","js");
  var cfg = window.FIRST_SPIN_CONFIG;
  var $  = function(s,c){return (c||document).querySelector(s);};
  var $$ = function(s,c){return Array.prototype.slice.call((c||document).querySelectorAll(s));};

  /* ---- analytics ---- */
  window.dataLayer = window.dataLayer || [];
  function gtag(){ window.dataLayer.push(arguments); }
  if (cfg.ga4MeasurementId){
    var s=document.createElement("script");s.async=true;
    s.src="https://www.googletagmanager.com/gtag/js?id="+encodeURIComponent(cfg.ga4MeasurementId);
    document.head.appendChild(s); gtag("js",new Date()); gtag("config",cfg.ga4MeasurementId);
  }
  function track(event,params){
    var p=Object.assign({event:event},params||{});
    window.dataLayer.push(p);
    if (window.gtag) window.gtag("event",event,params||{});
  }
  $$("[data-track]").forEach(function(el){
    el.addEventListener("click",function(){ track(el.getAttribute("data-track"),{location:el.getAttribute("data-track-loc")||"",page:document.body.getAttribute("data-page")||""}); });
  });

  /* ---- CTA routing: interest list / donate / newsletter ---- */
  $$('[data-cta="interest"]').forEach(function(el){
    if (cfg.interestFormUrl){ el.setAttribute("href",cfg.interestFormUrl); el.setAttribute("target","_blank"); el.setAttribute("rel","noopener"); }
    // else: leave existing href (falls back to the on-page interest form / #interest)
    el.addEventListener("click",function(){ track("interest_click",{location:el.getAttribute("data-track-loc")||""}); });
  });
  $$('[data-cta="donate"]').forEach(function(el){
    if (cfg.donateUrl){ el.setAttribute("href",cfg.donateUrl); el.setAttribute("target","_blank"); el.setAttribute("rel","noopener"); }
    el.addEventListener("click",function(){ track("donate_click",{location:el.getAttribute("data-track-loc")||""}); });
  });
  $$('[data-cta="newsletter"]').forEach(function(el){
    if (cfg.newsletterUrl){ el.setAttribute("href",cfg.newsletterUrl); el.setAttribute("target","_blank"); el.setAttribute("rel","noopener"); }
  });

  /* ---- mobile nav ---- */
  var nav=$(".nav"), toggle=$(".nav-toggle");
  if (toggle){
    toggle.addEventListener("click",function(){
      var open=nav.getAttribute("data-open")==="true";
      nav.setAttribute("data-open",String(!open));
      toggle.setAttribute("aria-expanded",String(!open));
    });
    $$(".nav-links a").forEach(function(a){
      a.addEventListener("click",function(){ if(a.getAttribute("href") && a.getAttribute("href").charAt(0)!=="#"){return;} nav.setAttribute("data-open","false"); toggle.setAttribute("aria-expanded","false"); });
    });
  }

  /* ---- forms (progressive enhancement) ---- */
  $$("form[data-form]").forEach(function(form){
    var b=$('button[type="submit"]',form); if(b) b.dataset.label=b.textContent;
    form.addEventListener("submit",function(e){
      e.preventDefault();
      if(!form.reportValidity()) return;
      var kind=form.getAttribute("data-form");
      var successEl=$(".form-success",form);
      var btn=$('button[type="submit"]',form);
      track("form_submit",{form:kind});
      function showSuccess(){
        if(successEl) successEl.setAttribute("data-state","show");
        $$("input,select,textarea",form).forEach(function(el){ if(el.type!=="submit"&&el.type!=="button"){ if(el.type==="checkbox"){el.checked=false;} else {el.value="";} } });
        if(successEl) successEl.scrollIntoView({behavior:"smooth",block:"center"});
      }
      if(cfg.formEndpoint){
        var data=new FormData(form); data.append("_form",kind);
        if(btn){btn.disabled=true;btn.textContent="Sending…";}
        fetch(cfg.formEndpoint,{method:"POST",body:data,headers:{"Accept":"application/json"}})
          .then(function(r){ if(!r.ok) throw new Error("bad"); return r; })
          .then(showSuccess)
          .catch(function(){ emailFallback(form,kind); showSuccess(); })
          .finally(function(){ if(btn){btn.disabled=false;btn.textContent=btn.dataset.label||"Submit";} });
      } else { emailFallback(form,kind); showSuccess(); }
    });
  });
  function emailFallback(form,kind){
    var lines=[];
    $$("input,select,textarea",form).forEach(function(el){
      if(!el.name||el.type==="file") return;
      if(el.type==="checkbox"){ lines.push(labelFor(el)+": "+(el.checked?"Yes":"No")); return; }
      if(el.value) lines.push(labelFor(el)+": "+el.value);
    });
    var subject="First Spin — "+kind+" form";
    var body=lines.join("\n")+"\n\n(Sent from firstspindjbootcamp.org)";
    window.open("mailto:"+cfg.contactEmail+"?subject="+encodeURIComponent(subject)+"&body="+encodeURIComponent(body),"_blank");
  }
  function labelFor(el){ return (el.labels&&el.labels[0])?el.labels[0].innerText.replace(/\*/g,"").trim():(el.name||"Field"); }

  /* ---- reveal on scroll ---- */
  var reduce=window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var revealAll=function(){ $$(".reveal").forEach(function(el){ el.classList.add("in"); }); };
  if(!reduce && "IntersectionObserver" in window){
    var io=new IntersectionObserver(function(entries){ entries.forEach(function(en){ if(en.isIntersecting){ en.target.classList.add("in"); io.unobserve(en.target); } }); },{rootMargin:"0px 0px -8% 0px",threshold:0.05});
    $$(".reveal").forEach(function(el){ io.observe(el); });
    setTimeout(revealAll,2500);
    window.addEventListener("load",function(){ setTimeout(revealAll,400); });
  } else { revealAll(); }

  /* ---- current year ---- */
  $$("[data-year]").forEach(function(el){ el.textContent=new Date().getFullYear(); });
})();
