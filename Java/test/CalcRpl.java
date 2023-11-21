
public class CalcRpl {
    private PileRPL pileRPL = new PileRPL();

    public void ajouter(double nombre) {
        pileRPL.push(nombre);
    }

    public void additionner() {
        if (pileRPL.vide()) {
            throw new IllegalStateException("La pile est vide.");
        }

        double somme = 0;
        while (!pileRPL.vide()) {
            somme += pileRPL.pop();
        }
        pileRPL.push(somme);
    }

    // Ajoutez d'autres méthodes pour d'autres opérations arithmétiques.

    public double obtenirResultat() {
        if (pileRPL.vide()) {
            throw new IllegalStateException("La pile est vide.");
        }
        return pileRPL.pop();
    }

    public static void main(String[] args) {
        CalcRpl calculatrice = new CalcRpl();

        calculatrice.ajouter(5.0);
        calculatrice.ajouter(3.0);
        System.out.println("BLABLABLA");
        System.out.println(calculatrice.toString());
        System.out.println("BLABLABLA 2");
        calculatrice.additionner();
        calculatrice.toString();

        System.out.println("Résultat : " + calculatrice.obtenirResultat());
    }
}
