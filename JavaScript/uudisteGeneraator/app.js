const newsTemplates = {
    technology: [
        "New AI model breaks records in image recognition tasks.",
        "Revolutionary smartphone with 3-day battery life unveiled.",
        "Tech giant announces quantum computing breakthrough.",
        "Innovative wearable tech can monitor health in real-time.",
        "Major security vulnerabilities discovered in popular apps.",
        "Flying car prototype successfully completes maiden flight."
    ],
    sports: [
        "Local team claims unexpected victory in championship finals.",
        "World record broken at international athletics competition.",
        "Star player signs record-breaking contract with new team.",
        "Underdog team defeats champions in stunning upset.",
        "Olympic committee announces new sport for 2028 games.",
        "Legendary coach announces retirement after 30-year career."
    ],
    economy: [
        "Stock markets reach all-time high amid economic recovery.",
        "New trade deal expected to boost global economy.",
        "Cryptocurrency values surge as major retailers adopt digital payments.",
        "Inflation rates stabilize after central bank intervention.",
        "Tech startup reaches unicorn status after latest funding round.",
        "Experts predict economic growth despite supply chain challenges."
    ]
};

function generateRandomDate() {
    const today = new Date();
    const randomDaysAgo = Math.floor(Math.random() * 7);
    const randomDate = new Date(today);
    randomDate.setDate(today.getDate() - randomDaysAgo);
    
    return randomDate.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

function createNewsItem(content, category) {
    const newsItem = document.createElement('div');
    newsItem.classList.add('news-item', category);
    
    const dateElement = document.createElement('div');
    dateElement.classList.add('news-date');
    dateElement.textContent = generateRandomDate();
    
    const contentElement = document.createElement('div');
    contentElement.classList.add('news-content');
    contentElement.textContent = content;
    
    newsItem.appendChild(dateElement);
    newsItem.appendChild(contentElement);
    
    return newsItem;
}

function generateNews() {
    const newsList = document.getElementById('news-list');
    const activeCategory = document.querySelector('.category-btn.active').dataset.category;
    
    newsList.innerHTML = '';
    
    const templates = newsTemplates[activeCategory];
    
    const shuffledTemplates = [...templates].sort(() => Math.random() - 0.5);
    
    const selectedTemplates = shuffledTemplates.slice(0, 3);
    
    selectedTemplates.forEach(template => {
        const newsItem = createNewsItem(template, activeCategory);
        newsList.appendChild(newsItem);
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const categoryButtons = document.querySelectorAll('.category-btn');
    categoryButtons.forEach(button => {
        button.addEventListener('click', function() {
            categoryButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
        });
    });
    
    document.getElementById('generate-btn').addEventListener('click', generateNews);
    
    document.getElementById('regenerate-btn').addEventListener('click', generateNews);
    
    document.getElementById('add-news-btn').addEventListener('click', function() {
        const newsContent = document.getElementById('news-content').value.trim();
        if (newsContent) {
            const activeCategory = document.querySelector('.category-btn.active').dataset.category;
            const newsItem = createNewsItem(newsContent, activeCategory);
            document.getElementById('news-list').appendChild(newsItem);
            document.getElementById('news-content').value = '';
        }
    });
    
    generateNews();
});