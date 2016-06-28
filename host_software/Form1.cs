/**
 * File name:        Form1.cs                                        
 * File description: File dedicated to the ES670 prototype project   
 *                   involving the HMI of the project                             
 *                                                                   
 * Authors:          Bruno de Souza Ferreira
 *                   Guilherme Kairalla Kolotelo
 *                   Guilherme Bersi Pereira              
 * Creation date:    26jun2016                                       
 * Revision date:    27jun2016                                       
 */

/* our package includes */
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO.Ports;
using System.IO;
using System.Threading;


/**
 * Namespace name:     Chart                       
 * Namespace description: scope of the HMI         
 * Input params:       n/a                         
 * Output params:      n/a                         
 */
namespace Chart
{
    /**
     * Class name:        Form1                         
     * Class description: main class of the hmi         
     * Input params:       n/a                          
     * Output params:      n/a                          
     */
    public partial class Form1 : Form
    {
        /* globals */
        string[] sSerialPorts = { "" }, sArrayData;
        string sData;
        double dTime = 0;
        double dVelocity = 0, dPosition = 0, dActuator = 0;

        /**
         * Method name:        Form1                        
         * Method description: initialize the HMI           
         * Input params:       n/a                          
         * Output params:      n/a                          
         */
        public Form1()
        {
            InitializeComponent();
        }

        /**
         * Method name:        search_Ports                 
         * Method description: seaches for serial port      
         *                     available                    
         * Input params:       bool bAdd - if true, adds    
         *                     the serial ports available   
         *                     to comboBox1                 
         * Output params:      n/a                          
         */
        void search_Ports(bool bAdd)
        {
            int iNum = sSerialPorts.Length;
            sSerialPorts = SerialPort.GetPortNames();
            if (iNum != sSerialPorts.Length || bAdd)
            {
                comboBox1.Items.Clear();
                for (int i = 0; i < sSerialPorts.Length; i++)
                {
                    comboBox1.Items.Add(sSerialPorts[i]);
                }
            }
        }

        /**
         * Method name:        Form1_Load                   
         * Method description: method that occurs when the  
         *                     Form1 (HMI) is loaded        
         * Input params:       object sender - the object   
         *                     that raised the event        
         *                     EventArgs e - contains info  
         *                     about the event              
         * Output params:      n/a                          
         */
        private void Form1_Load(object sender, EventArgs e)
        {
            search_Ports(true);
            try
            {
                serialPort.PortName = my_Config.Default.Port_Name;
                serialPort.BaudRate = my_Config.Default.Baud_Rate;
                Text = "Embedded Systems " + serialPort.PortName + "/" + Convert.ToString(serialPort.BaudRate); //Mostra no titulo do formulário o nome da serialPort seguido de "/" e o baudrate.
            }
            catch
            {
                MessageBox.Show("Error saving", "Error");
            }
        }

        /**
         * Method name:        button1_Click_1              
         * Method description: method that occurs when the  
         *                     button1 (Connect) is clicked 
         * Input params:       object sender - the object   
         *                     that raised the event        
         *                     EventArgs e - contains info  
         *                     about the event              
         * Output params:      n/a                          
         */
        private void button1_Click_1(object sender, EventArgs e)
        {
            try
            {
                dTime = 0;
                chart.Series["Velocity"].Points.Clear();
                chart.Update();
                serialPort.BaudRate = Convert.ToInt32(comboBox2.Text);
                serialPort.PortName = comboBox1.Text;
                Text = "Ebedded Systems " + comboBox1.Text + "/" + comboBox2.Text;
                serialPort.Open();
                serialPort.Write(" \n");
                Thread.Sleep(20);
                serialPort.Write(" \n");
            }
            catch{}
        }

        /**
         * Method name:        button2_Click_2              
         * Method description: method that occurs when the  
         *                     button2 (Disconnect) is      
         *                     clicked                      
         * Input params:       object sender - the object   
         *                     that raised the event        
         *                     EventArgs e - contains info  
         *                     about the event              
         * Output params:      n/a                          
         */
        private void button2_Click_2(object sender, EventArgs e)
        {
            serialPort.Close();
        }

        /**
         * Method name:        timer2_Tick                  
         * Method description: method that occurs when the  
         *                     timer2 reaches 1s. It        
         *                     updates the serial port      
         *                     combo box (comboBox1)        
         * Input params:       object sender - the object   
         *                     that raised the event        
         *                     EventArgs e - contains info  
         *                     about the event              
         * Output params:      n/a                          
         */
        private void timer2_Tick(object sender, EventArgs e)
        {
            search_Ports(false);
        }

        /**
         * Method name:        treatNewData                 
         * Method description: method that treats the data  
         *                     received through the         
         *                     serial port                  
         * Input params:       object sender - the object   
         *                     that raised the event        
         *                     EventArgs e - contains info  
         *                     about the event              
         * Output params:      n/a                          
         */
        private void treatNewData(object sender, EventArgs e)
        {
                sData=  serialPort.ReadLine();
                sArrayData = (sData.TrimEnd('\r','\n')).Split(' ');
                if (sArrayData.Length != 3)
                {
                    return;
                }
                dVelocity = Convert.ToDouble(sArrayData[0], System.Globalization.CultureInfo.InvariantCulture);
                dPosition = Convert.ToDouble(sArrayData[1], System.Globalization.CultureInfo.InvariantCulture);
                dActuator = Convert.ToDouble(sArrayData[2], System.Globalization.CultureInfo.InvariantCulture);
                    showNewData();                                   
            
        }

        /**
         * Method name:        showNewData                  
         * Method description: method that shows the data   
         *                     received through the         
         *                     serial port                  
         * Input params:       n/a                          
         * Output params:      n/a                          
         */
        private void showNewData()
        {
            double v = Convert.ToDouble(dVelocity);
            double p = Convert.ToDouble(dPosition);
            double a = Convert.ToDouble(dActuator);
            labelV.Text = Convert.ToString(v) + " rad/s";
            label2.Text = Convert.ToString(p) + " °";
            label9.Text = Convert.ToString(a) + "%";
            chart.Series[0].Points.AddXY(Math.Round(dTime,1),v);
            chart.Update();
                if (chart.Series[0].Points.Count > 100)
                {
                    chart.Series[0].Points.RemoveAt(0);
                    chart.Update();
                }                                                                        
            
        }

        /**
         * Method name:        serialPort_DataReceived      
         * Method description: method that activates when   
         *                     the data is received through 
         *                     the serial port              
         * Input params:       object sender - the object   
         *                     that raised the event        
         *                     SerialDataReceivedEventArgs e
         *                     - contains info about the    
         *                     event                        
         * Output params:      n/a                          
         */
        private void serialPort_DataReceived(object sender, SerialDataReceivedEventArgs e)
        {
            this.Invoke(new EventHandler(treatNewData));
        }

        /**
         * Method name:        Form1_FormClosing_1          
         * Method description: method that occurs when the  
         *                     Form1 (HMI) is closed        
         * Input params:       object sender - the object   
         *                     that raised the event        
         *                     EventArgs e - contains info  
         *                     about the event              
         * Output params:      n/a                          
         */
        private void Form1_FormClosing_1(object sender, FormClosingEventArgs e)
        {
            try
            {
                if (serialPort.IsOpen)
                {
                    serialPort.Close();
                }

            }
            catch
            { }

        }

        /**
         * Method name:        timer1_Tick                  
         * Method description: method that occurs when the  
         *                     timer2 reaches 100ms. It     
         *                     updates the time plotted     
         *                     on the x axis                
         * Input params:       object sender - the object   
         *                     that raised the event        
         *                     EventArgs e - contains info  
         *                     about the event              
         * Output params:      n/a                          
         */
        private void timer1_Tick(object sender, EventArgs e)
        {
            dTime = dTime + 0.1;
        }

        /**
         * Method name:        button3_Click_1              
         * Method description: method that occurs when the  
         *                     button3 (Send reference      
         *                     velocity) is clicked         
         * Input params:       object sender - the object   
         *                     that raised the event        
         *                     EventArgs e - contains info  
         *                     about the event              
         * Output params:      n/a                          
         */
        private void button3_Click_1(object sender, EventArgs e)
        {
            if (serialPort.IsOpen == true)          
                serialPort.WriteLine("v" + textBox1.Text);
        }

        /**
         * Method name:        button4_Click                
         * Method description: method that occurs when the  
         *                     button3 (Send Kp) is clicked 
         * Input params:       object sender - the object   
         *                     that raised the event        
         *                     EventArgs e - contains info  
         *                     about the event              
         * Output params:      n/a                       
         */
        private void button4_Click(object sender, EventArgs e)
        {
            if (serialPort.IsOpen == true)
            {
                serialPort.WriteLine("p" + Convert.ToString((Convert.ToDouble(textBox2.Text) * 10000), System.Globalization.CultureInfo.InvariantCulture));
            }
        }

        /**
         * Method name:        button5_Click                
         * Method description: method that occurs when the  
         *                     button3 (Send Ki) is clicked 
         * Input params:       object sender - the object   
         *                     that raised the event        
         *                     EventArgs e - contains info  
         *                     about the event              
         * Output params:      n/a
         */
        private void button5_Click(object sender, EventArgs e)
        {
            if (serialPort.IsOpen == true)
                serialPort.WriteLine("i" + Convert.ToString((Convert.ToDouble(textBox3.Text) * 10000), System.Globalization.CultureInfo.InvariantCulture));
        }

        /**
         * Method name:        button6_Click                
         * Method description: method that occurs when the  
         *                     button3 (Send Kd) is clicked 
         * Input params:       object sender - the object   
         *                     that raised the event        
         *                     EventArgs e - contains info  
         *                     about the event              
         * Output params:      n/a                          
         */
        private void button6_Click(object sender, EventArgs e)
        {
            if (serialPort.IsOpen == true)
                serialPort.WriteLine("d" + Convert.ToString((Convert.ToDouble(textBox4.Text) * 10000), System.Globalization.CultureInfo.InvariantCulture));
        }


       
    }
}
