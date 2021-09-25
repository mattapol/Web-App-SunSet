const contents = document.querySelector("#contents");
const loading = document.querySelector(".progress");

// Get news by newsAPI.org
const getNews = (category = "business") => {
  const apiKey = "adc24fa3173542c8a4713c0fa4224fc1";
  const url = `http://newsapi.org/v2/top-headlines?country=th&category=${category}&pageSize=100&apiKey=${apiKey}`;

  // Show loading
  loading.classList.add("show");

  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      if (data.status === "ok") {
        const articles = data.articles;
        articles.forEach((article) => {
          setTimeout(function () {
            addDataToDom(article);
            // Remove loading
            loading.classList.remove("show");
          }, 1000);
        });
      } else {
        console.log(data);
      }
    })
    .catch((err) => console.log(err));
};

// Render news data to DOM
function addDataToDom(article) {
  const newsElement = document.createElement("div");
  newsElement.classList.add("card-deck");
  newsElement.innerHTML = `
        <div class="card mb-3" style="max-width: 800px; margin: 15px; background-color: #FFC107;">
          <div class="row g-0" style="margin: 15px;">
              <div class="card-content">
                <span class="card-title"><h5 style="color: #ff0000">🕹${article.title}</h5></span>
                <p style="color: #115380">🎮${article.description}</p>
              </div>
            <div class="card-footer">
              <span>ที่มา - ${article.source.name}</span>
              <a href="${article.url}" target="_blank"> อ่านต่อ </a>
            </div>
          </div>
        </div>
    `;

  // Add news
  contents.appendChild(newsElement);
}

// Wait for DOM content to load
window.addEventListener("DOMContentLoaded", () => {
  // Get news and render
  getNews();
});

// Get active menu when click nav menu and get news with category
const lists = document.querySelectorAll("ul > li");
lists.forEach((li) => {
  li.addEventListener("click", function (e) {
    let current = document.querySelector(".active");
    current.classList.remove("active");

    e.target.parentElement.classList.add("active");

    let category = e.target.innerText.toLowerCase();

    // Clear contents
    contents.innerHTML = "";

    // Get news and add to contents
    getNews(category);
  });
});
