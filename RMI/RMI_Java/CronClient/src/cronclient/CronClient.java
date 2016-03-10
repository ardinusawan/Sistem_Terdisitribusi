
package cronclient;

import icron.CronDecodeInterface;
import java.io.File;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class CronClient {
    
    public static String[] event = new String[100000];
    public static int valEvent[] = new int[100000];
    public static int count =0;
    
    public static Map<String, Integer> countEvent(ArrayList<String> dbEvent){
        Map<String, Integer> seussCount = new HashMap<String,Integer>();
            for(String t: dbEvent) {
                Integer i = seussCount.get(t);
                if (i ==  null) {
                    i = 0;
                }
                seussCount.put(t, i + 1);
            }
        return seussCount;
    }
    
    public static void getDataFix(Map<String, Integer> map){
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
                        int exist = Arrays.asList(event).indexOf(entry.getKey());
                        if(exist>=0){
                            valEvent[exist] = valEvent[exist]+entry.getValue();
                        } else
                        {
                            event[count] = entry.getKey();
                            valEvent[count]= entry.getValue();
                            count++;
                        }
	}
    }
    
    public static void sortEvent(){
        int tempVal; String tempEv;
        for(int i=0;i<count;i++){
            for(int j=0;j<count;j++){
                if(valEvent[i] > valEvent[j]){
                    tempVal=valEvent[i];
                    tempEv=event[i];
                    valEvent[i]=valEvent[j];
                    event[i]=event[j];
                    valEvent[j]=tempVal;
                    event[j]=tempEv;                    
                }
            }
        }
        
    }
    public static void main(String[] args) {
        try{
            
            Registry myReg = LocateRegistry.getRegistry("192.168.43.204",1099);
            Registry myReg1 = LocateRegistry.getRegistry("192.168.43.207",1099);
            Registry myReg2 = LocateRegistry.getRegistry("192.168.43.123",1099);
            CronDecodeInterface c = (CronDecodeInterface)myReg.lookup("mycron");
            CronDecodeInterface c1 = (CronDecodeInterface)myReg1.lookup("mycron");
            CronDecodeInterface c2 = (CronDecodeInterface)myReg2.lookup("mycron");
            
            String dir = "\\\\192.168.43.128\\cron\\cron";
            //String dir = "\\\\192.168.88.79\\hnet-hon-var-log-02282006\\var\\log\\cron";
            int numserv=0;
                        
            for(int i=0;i<34;i++){
                File fin;
                if (i==0){
                    fin = new File(dir);
                } else
                { 
                    fin = new File(dir +"."+i);
                }
                if(numserv==0){
                    numserv++;
                    ArrayList<String> dbEvent = c.readFile1(fin);
                    Map<String, Integer> seussCount = countEvent(dbEvent);
                    Map<String, Integer> sortedMap = c.sortByComparator(seussCount);
                    getDataFix(sortedMap);
                    c.printMap(sortedMap);
                } 
                else if(numserv==1){
                    numserv++;
                    ArrayList<String> dbEvent1 = c1.readFile1(fin);
                    System.out.println(fin.toString());
                    Map<String, Integer> seussCount1 = countEvent(dbEvent1);
                    Map<String, Integer> sortedMap1 = c1.sortByComparator(seussCount1);
                    getDataFix(sortedMap1);
                    c1.printMap(sortedMap1);
                } 
                else if(numserv==2){
                    numserv=0;
                    String fin1 = "smb:"+fin.toString();
                    System.out.println(fin1.substring(0, 4)+"\\\\"+fin1.substring(4, fin1.length()));
                    fin = new File(fin1.substring(0, 4)+"\\\\"+fin1.substring(4, fin1.length()));
                    System.out.println(fin.toString());
                    ArrayList<String> dbEvent2 = c2.readFile1(fin);
                    Map<String, Integer> seussCount2 = countEvent(dbEvent2);
                    Map<String, Integer> sortedMap2 = c2.sortByComparator(seussCount2);
                    getDataFix(sortedMap2);
                    c2.printMap(sortedMap2);
                }
            }
            
            sortEvent();
            for(int i=0;i<10;i++){
                System.out.println(i+" "+event[i]+" "+valEvent[i]);
            }
                       
        }
        catch(Exception ex){
            ex.printStackTrace();
        }
    }
    
}
