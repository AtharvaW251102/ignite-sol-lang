const languageSelect = document.getElementById('languageSelect');
const getGreetingBtn = document.getElementById('getGreetingBtn');
const greetingMessage = document.getElementById('greetingMessage');

getGreetingBtn.addEventListener('click', async () => {
    const selectedLanguage = languageSelect.value;

    try {
        const response = await fetch('http://127.0.0.1:5000/hello?language=' + selectedLanguage);
        const data = await response.text();
        greetingMessage.textContent = data;
    } catch (error) {
        greetingMessage.textContent = 'Error fetching greeting.';
    }
});
