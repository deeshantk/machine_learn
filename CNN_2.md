# Sequential

keras Sequential model is a linear stack of layers. This will accepts an array and in that array, its going to have elements each of which will be an input layer. 
This can be done like -
> model = Sequential([l1,l2,l3]) where l1,l2,l3 are example of actual layers.
or like this
> model = Sequential()
  model.add(l1)
  model.add(l2)
  
  Now first layer is going to be a **Dense** layer. The required item that Dense needed is number of neurons that layer is supposed to have.Then what input shape it should expect.
  **Note- Only first layer of Sequential model needs to know the input shape**
  
