package messagequeue;

import com.rabbitmq.client.AMQP;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.Consumer;
import com.rabbitmq.client.DefaultConsumer;
import com.rabbitmq.client.Envelope;
import com.rabbitmq.client.MessageProperties;
import java.util.*;
import java.io.*;
import java.util.logging.Level;
import java.util.logging.Logger;


public class NewTask {
    
  private static String[] event = new String[100000];
  private static int valEvent[] = new int[100000];
  private static int count =0;

  private static final String TASK_QUEUE_NAME = "task_queue";
  
  //convert data to string
  private static void getDataFix(Map<String, Integer> map){
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
  
  //sorting event
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
    
  private static String getMessage(String[] strings) {
    if (strings.length < 1)
      return "Hello World.....!";
    return joinStrings(strings, " ");
  }

  private static String joinStrings(String[] strings, String delimiter) {
    int length = strings.length;
    if (length == 0) return "";
    StringBuilder words = new StringBuilder(strings[0]);
    for (int i = 1; i < length; i++) {
      words.append(delimiter).append(strings[i]);
    }
    return words.toString();
  }
  
  private static String[] path(){
      String p[] = new String[34];
      for(int i=0;i<1;i++){
          if(i==0){
              p[i] ="E:\\ITS\\KULIAH\\SEMESTER 6\\SISTER\\cron\\cron";
          } else{
              p[i] ="E:\\ITS\\KULIAH\\SEMESTER 6\\SISTER\\cron\\cron."+i;
          }
      }
      return p;
  }
  
  public static void main(String[] argv) throws Exception {
    CronDecodeInterface c = new CronImplementation();
    String[] p = path();
    ConnectionFactory factory = new ConnectionFactory();
    factory.setHost("localhost");
    Connection connection = factory.newConnection();
    Channel channel = connection.createChannel();
    
    for(int i=0;i<p.length;i++){
        File fin = new File(p[i]);
        ArrayList<String> dbEvent = c.readFile1(fin);
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        DataOutputStream out = new DataOutputStream(baos);
        for (String element : dbEvent) {
            out.writeUTF(element);
        }
        byte[] bytes = baos.toByteArray();
        channel.queueDeclare(TASK_QUEUE_NAME, true, false, false, null);
        channel.basicPublish("", TASK_QUEUE_NAME,
                            MessageProperties.PERSISTENT_TEXT_PLAIN,
                            bytes);
        String dat = p[i].substring(p[i].length()-6, p[i].length());
        System.out.println(" [x] Sent '" + dat + "'");
        
        //get output from server
        final Consumer consumer = new DefaultConsumer(channel) {
            @Override
            public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) throws IOException {
                Map<String, Integer> sortedMap = new HashMap<String, Integer>();
                try(ByteArrayInputStream b = new ByteArrayInputStream(body)){
                    try(ObjectInputStream o = new ObjectInputStream(b)){
                        sortedMap = (Map<String, Integer>) o.readObject();
                    } catch (ClassNotFoundException ex) {
                      Logger.getLogger(NewTask.class.getName()).log(Level.SEVERE, null, ex);
                    }
                }  
              getDataFix(sortedMap);
            }
        };
        
        channel.close();
        connection.close();
    }
    
//    ConnectionFactory factory = new ConnectionFactory();
//    factory.setHost("localhost");
//    Connection connection = factory.newConnection();
//    Channel channel = connection.createChannel();
//
//    channel.queueDeclare(TASK_QUEUE_NAME, true, false, false, null);
//
//    String message = getMessage(argv);
//
//    channel.basicPublish("", TASK_QUEUE_NAME,
//                        MessageProperties.PERSISTENT_TEXT_PLAIN,
//                        message.getBytes("UTF-8"));
//    System.out.println(" [x] Sent '" + message + "'");
//
//    channel.close();
//    connection.close();
  }

}