// Função para formatar a data para exibição
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('pt-BR', options);
}

const newsContainer = document.getElementById('news-container');
const newsDateInput = document.getElementById('news-date');
const noNewsMessage = document.getElementById('no-news-message');
const legalAnalysisModal = document.getElementById('legalAnalysisModal');
const modalTitle = document.getElementById('modalTitle');
const modalContent = document.getElementById('modalContent');
const modalLoading = document.getElementById('modalLoading');

// Função para exibir o modal
function openModal() {
    legalAnalysisModal.style.display = 'flex';
}

// Função para fechar o modal
function closeModal() {
    legalAnalysisModal.style.display = 'none';
    modalContent.innerHTML = ''; // Limpa o conteúdo ao fechar
    modalLoading.classList.add('hidden'); // Esconde o loading
}

// Função para gerar a análise jurídica usando a API Gemini
async function generateLegalAnalysis(title, summary) {
    openModal();
    modalTitle.textContent = 'Análise Jurídica para: ' + title;
    modalContent.innerHTML = '';
    modalLoading.classList.remove('hidden'); // Mostra o loading

    try {
        const response = await fetch('/api/generate_analysis', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title: title, summary: summary })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();

        if (result.analysis) {
            modalContent.innerHTML = `<p>${result.analysis}</p>`;
        } else {
            modalContent.innerHTML = '<p class="text-red-500">Não foi possível gerar a análise. Tente novamente.</p>';
        }
    } catch (error) {
        console.error('Erro ao chamar a API Gemini:', error);
        modalContent.innerHTML = '<p class="text-red-500">Ocorreu um erro ao conectar com o serviço de análise. Por favor, tente novamente mais tarde.</p>';
    } finally {
        modalLoading.classList.add('hidden'); // Esconde o loading
    }
}

// Função para renderizar as notícias
async function renderNews(date) {
    newsContainer.innerHTML = ''; // Limpa o container de notícias
    noNewsMessage.classList.add('hidden'); // Esconde a mensagem de "nenhuma notícia"

    try {
        const response = await fetch(`/api/news?date=${date}`); // Chama sua nova API
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const filteredNews = await response.json();

        if (filteredNews.length === 0) {
            noNewsMessage.classList.remove('hidden'); // Mostra a mensagem se não houver notícias
            return;
        }

        // Limita a 20 notícias, se houver mais (já feito na API, mas bom ter aqui tbm)
        const newsToDisplay = filteredNews.slice(0, 20);

        newsToDisplay.forEach(news => {
            const newsCard = document.createElement('div');
            newsCard.className = 'bg-white rounded-xl shadow-md overflow-hidden transform transition duration-300 hover:scale-105 hover:shadow-lg';
            newsCard.innerHTML = `
                <img src="${news.image}" alt="${news.title}" class="placeholder-image">
                <div class="p-6">
                    <span class="inline-block bg-peck-light-teal text-peck-dark-teal text-xs font-semibold px-3 py-1 rounded-full mb-3">
                        ${news.category}
                    </span>
                    <h3 class="text-xl font-semibold text-peck-dark-teal mb-2">${news.title}</h3>
                    <p class="text-gray-600 text-sm mb-4">${news.summary}</p>
                    <span class="text-xs text-gray-400">Publicado em: ${formatDate(news.date)}</span>
                    <button onclick="generateLegalAnalysis('${news.title.replace(/'/g, "\\'")}', '${news.summary.replace(/'/g, "\\'")}')"
                            class="mt-4 w-full bg-peck-accent-green text-peck-dark-teal font-bold py-2 px-4 rounded-full hover:bg-opacity-90 transition duration-300 ease-in-out flex items-center justify-center">
                        Análise Jurídica ✨
                    </button>
                </div>
            `;
            newsContainer.appendChild(newsCard);
        });
    } catch (error) {
        console.error('Erro ao buscar notícias:', error);
        newsContainer.innerHTML = `<p class="text-red-500">Ocorreu um erro ao carregar as notícias. Por favor, tente novamente.</p>`;
        noNewsMessage.classList.add('hidden'); // Esconde a mensagem de "nenhuma notícia" em caso de erro.
    }
}

// Define a data atual como padrão no campo de data
const today = new Date();
const year = today.getFullYear();
const month = String(today.getMonth() + 1).padStart(2, '0'); // Mês é 0-indexado
const day = String(today.getDate()).padStart(2, '0');
const defaultDate = `${year}-${month}-${day}`;
newsDateInput.value = defaultDate;

// Renderiza as notícias para a data padrão ao carregar a página
renderNews(defaultDate);

// Adiciona um listener para o evento 'change' no seletor de data
newsDateInput.addEventListener('change', (event) => {
    const selectedDate = event.target.value;
    renderNews(selectedDate);
});