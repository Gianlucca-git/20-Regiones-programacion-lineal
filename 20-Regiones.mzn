var int : n ;


array[1..n] of int: X_INTRODUCED_1_       ; %ventiladores
array [1..n] of int: X_INTRODUCED_3_      ; %personal
array [1..n] of int: X_INTRODUCED_5_      ; %costo
array [1..n] of int: X_INTRODUCED_9_      ; %cualificacion
array [1..(n+1)] of int: X_INTRODUCED_12_ ; %z
%%array [1..7] of int: X_INTRODUCED_1_ = [1,1,2,2,1,1,1];%ventiladores
%%array [1..7] of int: X_INTRODUCED_3_ = [3,1,1,1,4,2,2];%personal
%array [1..7] of int: X_INTRODUCED_5_ = [3500000,5000000,1500000,4000000,4000000,5000000,4500000];%costo
%array [1..3] of int: X_INTRODUCED_9_ = [-2,-4,-3];%cualificacion
%array [1..8] of int: X_INTRODUCED_12_ = [1,-6,-3,-4,-1,-5,-2,-7];%z


var int: X1:: output_var;
var int: X2:: output_var;
var int: X3:: output_var;
var int: X4:: output_var;
var int: X5:: output_var;
var int: X6:: output_var;
var int: X7:: output_var;
var int: Z:: is_defined_var:: output_var;


constraint int_lin_le(X_INTRODUCED_1_,[X1,X2,X3,X4,X5,X6,X7],1000);
constraint int_lin_le(X_INTRODUCED_3_,[X1,X2,X3,X4,X5,X6,X7],2000);
constraint int_lin_le(X_INTRODUCED_5_,[X1,X2,X3,X4,X5,X6,X7],3500000000);
constraint int_lin_le(X_INTRODUCED_9_,[X1,X2,X3,X4,X5,X6,X7],-1000);
constraint int_lin_eq(X_INTRODUCED_12_,[Z,X1,X2,X3,X4,X5,X6,X7],0):: defines_var(Z);
constraint int_le(0,X1);
constraint int_le(0,X2);
constraint int_le(0,X3);
constraint int_le(0,X4);
constraint int_le(0,X5);
constraint int_le(0,X6);
constraint int_le(0,X7);
solve  maximize Z;