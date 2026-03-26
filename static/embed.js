(function () {
  function loadAds() {
    const ads = document.querySelectorAll(".adabsurd");

    ads.forEach(el => {
      const tone = el.dataset.tone || "corporate";
      const chaos = el.dataset.chaos || "50";

      fetch(`https://web-production-ee380.up.railway.app/ad?tone=${tone}&chaos=${chaos}`)
        .then(res => res.json())
        .then(ad => {
          el.innerHTML = `
            <div style="
              background:${ad.bg_color};
              color:white;
              padding:12px;
              border-radius:10px;
              font-family:sans-serif;
              box-shadow:0 4px 12px rgba(0,0,0,0.2);
            ">
              <strong>${ad.title}</strong>
              <p>${ad.tagline}</p>
              <button style="
                margin-top:8px;
                padding:6px 10px;
                border:none;
                border-radius:6px;
                cursor:pointer;
              ">${ad.cta}</button>
              <div style="font-size:10px;opacity:0.6;margin-top:6px;">
                Powered by AdAbsurd™
              </div>
            </div>
          `;
        })
        .catch(() => {
          el.innerHTML = "<div style='color:red'>AdAbsurd failed to load</div>";
        });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", loadAds);
  } else {
    loadAds();
  }
})();
