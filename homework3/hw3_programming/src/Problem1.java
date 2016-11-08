import Jama.Matrix;

import java.io.*;

/**
 * Created by WangJian on 2016/11/2.
 */
public class Problem1 {
    private W getData(File file){
        Double[] x1Array;
        Double[] x2Array;
        W w = null;
        try (BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(new FileInputStream(file)))) {
            String[] x1Line = bufferedReader.readLine().split("\\t");
            String[] x2Line = bufferedReader.readLine().split("\\t");
            x1Array = new Double[x1Line.length];
            x2Array = new Double[x2Line.length];
            for (int i = 0;i<x1Line.length;i++){
                x1Array[i] = Double.valueOf(x1Line[i]);
                x2Array[i] = Double.valueOf(x2Line[i]);
            }
            w = new W(x1Array,x2Array);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        if(w!=null){
            return w;
        }else{
            throw new RuntimeException("Null Data");
        }
    }
    public void problemA(){
        File file1 = new File("./w1.txt");
        File file2 = new File("./w2.txt");

        W w1 = getData(file1);
        W w2 = getData(file2);


    }
    public static void main(String args[]){
        Problem1 problem1 = new Problem1();
        problem1.problemA();
    }
}

class W{
    Double[] x0Array;
    Double[]x1Array;
    Double[]x2Array;
    W(Double[]x1Array,Double[]x2Array){
        this.x1Array = x1Array;
        this.x2Array = x2Array;
        this.x0Array = new Double[x1Array.length];
        for(int i = 0;i<x0Array.length;i++){
            x0Array[i]=1.0;
        }
    }
}
