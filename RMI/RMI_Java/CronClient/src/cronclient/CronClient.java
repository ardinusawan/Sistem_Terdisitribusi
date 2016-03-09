
package cronclient;

import icron.CronDecodeInterface;
import java.io.File;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class CronClient {

    public static void main(String[] args) {
        try{
            Registry myReg = LocateRegistry.getRegistry("127.0.0.1",1099);
//            Registry myReg1 = LocateRegistry.getRegistry("192.168.88.79",1099);
//            Registry myReg2 = LocateRegistry.getRegistry("xxx.xxx.xxx.xxx",1099);
            CronDecodeInterface c = (CronDecodeInterface)myReg.lookup("mycron");
//            CronDecodeInterface c1 = (CronDecodeInterface)myReg1.lookup("mycron");
//            CronDecodeInterface c2 = (CronDecodeInterface)myReg2.lookup("mycron");
            
            String dir = "\\\\192.168.88.79\\hnet-hon-var-log-02282006\\var\\log\\cron";
            
            for(int i=0;i<34;i++){
                File fin;
                if (i==0){
                    fin = new File(dir);
                } else
                {
                    fin = new File(dir +"."+i);
                }
                System.out.println(fin.toString());
            }
            
            
            //File fin = new File(dir.getCanonicalPath() + File.separator + "cron.2");
            //ArrayList<String> dbEvent = c.readFile1(fin);
            
//            Map<String, Integer> seussCount = new HashMap<String,Integer>();
//            for(String t: dbEvent) {
//                Integer i = seussCount.get(t);
//                if (i ==  null) {
//                    i = 0;
//                }
//                seussCount.put(t, i + 1);
//            }
//            
//             Map<String, Integer> sortedMap = c.sortByComparator(seussCount);
//             c.printMap(sortedMap);
        }
        catch(Exception ex){
            ex.printStackTrace();
        }
    }
    
}
