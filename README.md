# MultipleLinearRegression

Problem: Creare a model that predicts the profit of a company depending on it's various expenditures and circumstances. 
Formalism: 
         Task(T) : Find the corelation between the profit of the company to the various attributes that affected its profit.
         Experience(E): A previous dataset having the list of profits depending on the various expenditures of the company.
         Perfomance(P): Selecting only those attributes which contribute maximum to the value of profit.

Assumptions: All the attributes, initially affect the profit variable.
             None of the attributes are removed in the beginning.
             Location of the company matters so the nominal attribute must be encoded to make use of it in the model.
             

Motivation: Very first practice on multiple regression problems.
Solution Benefit: Helps the company understand where to focus more on its expenditures to maximise the profits.
Solution Use: Used for a business perspective to untimalety grow the company's horizons.

How to solve the problem:
                         By using the method of backward elimination to find out which attributes decide it's maximum profits and to retain them in the model and remove the rest of the attributes.
