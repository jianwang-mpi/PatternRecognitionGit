import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.concurrent.SynchronousQueue;

/**
 * Created by WangJian on 2016/9/30.
 */
public class LDF {
    File trainLabel = new File("./train-labels.idx1-ubyte");
    public void train() throws Exception{
        byte[] Int = new byte[4];
        FileInputStream fileInputStream = new FileInputStream(trainLabel);
        fileInputStream.read(Int);
        System.out.println(Integer.)
    }
    public static void main(String args[]) throws Exception{
        LDF ldf = new LDF();
        ldf.train();
    }
}
