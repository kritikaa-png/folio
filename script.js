const themeToggle = document.querySelector('#theme-toggle');
themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark');
    const isDark = document.body.classList.contains('dark');
    themeToggle.textContent = isDark ? '\u2600\uFE0F' : '\uD83C\uDF19'; // ☀️ or 🌙
});
const toTop = document.querySelector('#to-top');
window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        toTop.classList.add('show');
    } else {
        toTop.classList.remove('show');
    }
});
toTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});
const revealItems = document.querySelectorAll('.reveal');
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
        }
    });
}, {
    threshold: 0.15 
});
revealItems.forEach((item) => observer.observe(item));
const buttons = document.querySelectorAll("[data-filter]");
const cards = document.querySelectorAll(".project-card");
const count = document.getElementById("count");

buttons.forEach(button => {
    button.addEventListener("click", () => {
        const filter = button.dataset.filter;
        let visibleCount = 0;

        cards.forEach(card => {
            if (
                filter === "all" ||
                card.classList.contains(filter)
            ) {
                card.classList.remove("hide");
                visibleCount++;
            } else {
                card.classList.add("hide");
            }
        });

        count.textContent = visibleCount;
    });
});
fetch("projects.json")
  .then(response => response.json())
  .then(projects => {

    const container =
      document.getElementById("projects-container");

    projects.forEach(project => {

      const card = document.createElement("div");

      card.classList.add("project-card");

      card.innerHTML = `
        <h3>${project.name}</h3>
        <p>${project.description || "No description"}</p>
        <p>⭐ ${project.stars}</p>
        <a href="${project.url}" target="_blank">
          View Repository
        </a>
      `;

      container.appendChild(card);
    });

  });