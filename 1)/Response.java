public class Response {
    public static void main(String[] args) {
        int index = 13, SOMA = 0, K = 0;

        
        while (K < index) {
            K = K + 1;
            SOMA = SOMA + K;
        }

        System.out.println(SOMA); // Resposta: 91
    }
}
