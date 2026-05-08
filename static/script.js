/* Frontend JS — talks to the Flask /api endpoints */

const searchInput  = document.getElementById("searchInput");
const rarityFilter = document.getElementById("rarityFilter");
const sortSelect   = document.getElementById("sortSelect");
const searchBtn    = document.getElementById("searchBtn");
const resultsBody  = document.getElementById("resultsBody");
const resultInfo   = document.getElementById("resultInfo");

/* 1) Load rarity options from DB on page load */
async function loadRarities() {
  const res = await fetch("/api/rarities");
  const rarities = await res.json();
  rarities.forEach(r => {
    const opt = document.createElement("option");
    opt.value = r;
    opt.textContent = r;
    rarityFilter.appendChild(opt);
  });
}

/* 2) Fetch and render skins */
async function loadSkins() {
  const params = new URLSearchParams({
    q:      searchInput.value,
    rarity: rarityFilter.value,
    sort:   sortSelect.value
  });
  const res   = await fetch("/api/skins?" + params.toString());
  const skins = await res.json();

  resultsBody.innerHTML = "";

  if (skins.length === 0) {
    resultsBody.innerHTML =
      `<tr><td colspan="5" class="no-results">No skins found. Try a different search.</td></tr>`;
    resultInfo.textContent = "0 results";
    return;
  }

  skins.forEach(skin => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td><img class="skin-img" src="${skin.image_url}" alt="${skin.name}"
               onerror="this.style.opacity=0.3"></td>
      <td>
        <span class="skin-name">${skin.name}</span>
        <span class="skin-weapon">${skin.weapon}</span>
      </td>
      <td>${skin.wear}</td>
      <td><span class="rarity-badge rarity-${skin.rarity.replace(/[^A-Za-z]/g,'')}">${skin.rarity}</span></td>
      <td class="price">$${skin.market_value.toFixed(2)}</td>
    `;
    resultsBody.appendChild(tr);
  });

  resultInfo.textContent = `${skins.length} result${skins.length !== 1 ? "s" : ""} found`;
}

/* 3) Wire up events */
searchBtn.addEventListener("click", loadSkins);
searchInput.addEventListener("keyup", e => { if (e.key === "Enter") loadSkins(); });
rarityFilter.addEventListener("change", loadSkins);
sortSelect.addEventListener("change",   loadSkins);

/* 4) Initial load */
loadRarities().then(loadSkins);
