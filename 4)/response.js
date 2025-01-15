// Faturamento por estado
const faturamentoPorEstado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
};


function calcularPercentuais(faturamentoPorEstado) {

    const faturamentoTotal = Object.values(faturamentoPorEstado).reduce((acc, curr) => acc + curr, 0);
    
    for (let estado in faturamentoPorEstado) {
        const percentual = (faturamentoPorEstado[estado] / faturamentoTotal) * 100;
        console.log(`Percentual de ${estado}: ${percentual.toFixed(2)}%`);
    }
}

calcularPercentuais(faturamentoPorEstado);


// Percentual de SP: 37.53%
// Percentual de RJ: 20.29%
// Percentual de MG: 16.17%
// Percentual de ES: 15.03%
// Percentual de Outros: 10.98%