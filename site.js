(function () {
  "use strict";

  var nav = document.querySelector(".nav");
  var toggle = document.querySelector(".nav-toggle");
  var year = document.getElementById("yil");

  if (year) {
    year.textContent = String(new Date().getFullYear());
  }

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  document.querySelectorAll(".sub-toggle").forEach(function (btn) {
    btn.addEventListener("click", function (event) {
      event.preventDefault();
      event.stopPropagation();
      var parent = btn.closest(".has-sub");
      var willOpen = !parent.classList.contains("is-open");
      document.querySelectorAll(".has-sub").forEach(function (item) {
        item.classList.remove("is-open");
        var other = item.querySelector(".sub-toggle");
        if (other) other.setAttribute("aria-expanded", "false");
      });
      if (willOpen) {
        parent.classList.add("is-open");
        btn.setAttribute("aria-expanded", "true");
      }
    });
  });

  document.addEventListener("click", function (event) {
    if (!nav) return;
    if (!nav.contains(event.target) && toggle && !toggle.contains(event.target)) {
      nav.classList.remove("is-open");
      if (toggle) toggle.setAttribute("aria-expanded", "false");
      document.querySelectorAll(".has-sub").forEach(function (item) {
        item.classList.remove("is-open");
        var other = item.querySelector(".sub-toggle");
        if (other) other.setAttribute("aria-expanded", "false");
      });
    }
  });

  document.querySelectorAll(".faq-item button").forEach(function (button) {
    button.addEventListener("click", function () {
      var item = button.closest(".faq-item");
      var expanded = button.getAttribute("aria-expanded") === "true";
      document.querySelectorAll(".faq-item").forEach(function (other) {
        other.classList.remove("is-open");
        var otherBtn = other.querySelector("button");
        if (otherBtn) otherBtn.setAttribute("aria-expanded", "false");
      });
      if (!expanded) {
        item.classList.add("is-open");
        button.setAttribute("aria-expanded", "true");
      }
    });
  });

  function stripControl(value) {
    return String(value || "").replace(/[\u0000-\u001F\u007F]/g, "").trim();
  }

  function hasInjection(value) {
    return /<\s*\/?\s*[a-z!]|javascript:|data:text\/html|on\w+\s*=/i.test(value);
  }

  function clip(value, max) {
    return value.length > max ? value.slice(0, max) : value;
  }

  var form = document.getElementById("teklif-formu");
  if (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var status = document.getElementById("form-durum");
      var ad = stripControl(form.ad.value);
      var telefon = stripControl(form.telefon.value);
      var ilce = stripControl(form.ilce.value);
      var mesaj = stripControl(form.mesaj.value);

      if (hasInjection(ad) || hasInjection(telefon) || hasInjection(ilce) || hasInjection(mesaj)) {
        if (status) status.textContent = "Metinde HTML veya betik izi olmamalı. Düz yazı yazın.";
        return;
      }

      if (ad.length < 2 || mesaj.length < 8) {
        if (status) status.textContent = "Ad ve işin kısa tarifi gerekli.";
        return;
      }

      if (!/^[0-9+\s()]{10,18}$/.test(telefon)) {
        if (status) status.textContent = "Telefonu 05xx xxx xx xx biçiminde yazın.";
        return;
      }

      ad = clip(ad, 80);
      telefon = clip(telefon, 18);
      ilce = clip(ilce, 40);
      mesaj = clip(mesaj, 400);

      var text =
        "Merhaba, Antalya Modern Mermer'den teklif istiyorum.\n" +
        "Ad: " + ad + "\n" +
        "Telefon: " + telefon + "\n" +
        "İlçe: " + ilce + "\n" +
        "İş: " + mesaj;

      window.location.href = "https://wa.me/905333171146?text=" + encodeURIComponent(text);
    });
  }
})();
