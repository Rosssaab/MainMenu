document.addEventListener('DOMContentLoaded', function() {
    const themeSelect = document.getElementById('theme-select');
    const themeLink = document.getElementById('theme-style');

    function changeTheme(theme) {
        if (theme === 'default') {
            themeLink.href = 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css';
        } else {
            themeLink.href = `https://cdn.jsdelivr.net/npm/bootswatch@5.3.0/dist/${theme}/bootstrap.min.css`;
        }
    }

    function saveTheme(theme) {
        localStorage.setItem('selectedTheme', theme);
    }

    function loadSavedTheme() {
        return localStorage.getItem('selectedTheme') || 'default';
    }

    themeSelect.addEventListener('change', function() {
        changeTheme(this.value);
        saveTheme(this.value);
    });

    // Load and apply saved theme
    const savedTheme = loadSavedTheme();
    themeSelect.value = savedTheme;
    changeTheme(savedTheme);
});
