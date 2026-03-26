(function () {
  function loadAds() {
    const ads = document.querySelectorAll(".adabsurd");

    const sizes = {
      "728x90": { w: 728, h: 90 },
      "300x250": { w: 300, h: 250 },
      "320x50": { w: 320, h: 50 }
    };

    ads.forEach(el => {
      const tone = el.dataset.tone || "corporate";
      const chaos = el.dataset.chaos || "50";
      const format = el.dataset.format || "300x250";

      const size = sizes[format] || sizes["300x250"];

      fetch(`https://YOUR-RAILWAY-URL/ad?tone=${tone}&chaos=${chaos}&format=${format}`)
        .then(res => res.json())
        .then(ad => {

          let content = "";

          if (ad.image) {
            content = `<img src="https://YOUR-RAILWAY-URL${ad.image}" 
              style="width:100%; height:100%; object-fit:cover; border-radius:8px;" />`;
          } else {
            content = `
              <div>
                <strong>${ad.title}</strong>
                <p>${ad.tagline}</p>
                <small>${ad.price}</small>
              </div>
            `;
          }

          el.innerHTML = `
            <div style="
              width:${size.w}px;
              height:${size.h}px;
              background:${ad.bg_color};
              color:white;
              border-radius:8px;
              overflow:hidden;
              font-family:sans-serif;
              display:flex;
              align-items:center;
              justify-content:center;
              cursor:pointer;
            ">
              ${content}
            </div>
          `;
        })
        .catch(err => {
          console.error("AdAbsurd error:", err);
          el.innerHTML = "<div style='color:red'>Ad failed</div>";
        });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", loadAds);
  } else {
    loadAds();
  }
})();