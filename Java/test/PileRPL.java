import java.util.ArrayList;
import java.util.List;

public class PileRPL {
    private List<Double> pile = new ArrayList<>();
    // Ajouter dans la pile une valeur
    public void push(double val) {
        pile.add(val);
    }

    public double pop() {
        if (!vide()) {
            int index = pile.size() - 1;
            double poppedValue = pile.get(index);
            pile.remove(index);
            return poppedValue;
        } else {
            throw new IllegalStateException("La pile est vide.");
        }
    }

    public boolean vide() {
        return pile.isEmpty();
    }

    public String toString(){
        System.out.println("toString");
        String result = "";
        
        //for (int i=pile.size(); i >= 0; i--){
        //    result += "|    " + pile.get(i) + "    |\n";
        //}
        for (int i=0; i < pile.size(); i++){
            System.out.println("i: " + i + "val: " + pile.get(i));
        }
        return result;
    }
}

