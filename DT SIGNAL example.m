dtsig = input("Type '1' to input value vector");

if dtsig == 1
 x = input("Number of data points:");
 start = input("Starting point of data point on axis:");
 n1 = start:start+x-1;
 val1 = input("Enter values with [] around it:");
 [r,c] = size(val1);
 res = show_plot(n1,val1,c,x);  
else
 disp("Please enter valid number")
end

function plots = plotpoints(n1,val1)
 plots = stem(n1,val1,'MarkerFaceColor','red');
 xlim([n1(1)-1,n1(end)+1]);
 title("Discrete Signal");
 xlabel("Data points");
 ylabel("Values");
 yline(0,'r')
 xline(0,'r')
 grid on;

end
 
function res = show_plot(n1,val1,c,x)

  if (c==x) 
    disp("Same vector size.")
    res = plotpoints(n1,val1);
    
 elseif (c>x)
    disp("Data vector size is larger than number of data points.")
    res = plotpoints(n1,val1(1:x));
    
  else
    disp("Data vector size is smaller than number of data points.")
    val1(end+1:end+x-c)=0;
    res = plotpoints(n1,val1);
    
  end
 
end

