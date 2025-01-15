using System;

class Program
{
    static void Main()
    {
        string inverterString(string str)
        {
            char[] array = str.ToCharArray();
            Array.Reverse(array);
            return new string(array);
        }
        
        string stringOriginal = "Exemplo de String";
        string stringInvertida = inverterString(stringOriginal);
        
        Console.WriteLine("String invertida: " + stringInvertida);
    }
}
