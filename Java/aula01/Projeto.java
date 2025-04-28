import java.util.Scanner;
public class Projeto{
    static public void main(String[] args){
        Scanner input = new Scanner(System.in);
        int numRandom = (int)(Math.random() * 100) + 1;
        int num = 0;
        int tentativas = 0;
        while(num != numRandom){
            System.out.println("Digite um número: ");
            num = input.nextInt();
            tentativas++;
            if(num > numRandom){
                System.out.println("O número digitado é maior do que o sorteado.");
            }
            else if(num < numRandom){
                System.out.println("O número digitado é menor do que o sorteado");
            }
        }
        System.out.println("Você acertou o número!");
        System.out.println("Você precisou de: " + tentativas + " tentativa(s)!");
        input.close();
    }
}