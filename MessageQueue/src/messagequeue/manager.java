package messagequeue;

import com.rabbitmq.client.AMQP;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.Consumer;
import com.rabbitmq.client.DefaultConsumer;
import com.rabbitmq.client.Envelope;
import com.rabbitmq.client.MessageProperties;
import java.io.*;
import java.util.*;
import java.util.logging.Level;
import java.util.logging.Logger;

public class manager {
    private static String TASK_QUEUE_NAME = "sinkering";
    
    public static String[] event = new String[100000];
    public static int valEvent[] = new int[100000];
    public static int count =0;
    //get data to String
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
    
    
    public static void main(String args[])throws Exception{
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        final Connection connection = factory.newConnection();
        final Channel channel = connection.createChannel();

        channel.queueDeclare(TASK_QUEUE_NAME, true, false, false, null);
        System.out.println(" [*] Waiting for messages. To exit press CTRL+C");
        channel.basicQos(1);

        final Consumer consumer = new DefaultConsumer(channel) {
          @Override
          public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) throws IOException {
            ByteArrayInputStream byteIn = new ByteArrayInputStream(body);
            ObjectInputStream in = new ObjectInputStream(byteIn);
              try {
                  Map<String, Integer> data2 = (Map<String, Integer>) in.readObject();
                  getDataFix(data2);
                  sortEvent();
                  System.out.println("\n\nTop 10 Cron Event : ");
                    for(int i=0;i<10;i++){
                        int j=i+1;
                        System.out.println(j+" "+event[i]+" "+valEvent[i]);
                    }
              } catch (ClassNotFoundException ex) {
                  Logger.getLogger(manager.class.getName()).log(Level.SEVERE, null, ex);
              }
           }
        };
        channel.basicConsume(TASK_QUEUE_NAME, false, consumer);
//        channel.queueDelete(TASK_QUEUE_NAME);
    }
}