from rectangle import Rectangle
class Square(Rectangle):
    def __init__ (self,length):
        super().__init__(length,length)
        
    def set_length(self,new_length):
        """
        Change the length of the rectangle.

        :param new_length: length (horizontal dimension) of rectangle.  Must be >= 0.  Otherwise, no change is made.
        """
        if new_length>=0 :
            self.length=new_length
            self.height=new_length
            if self.has_been_drawn : #Only redraw rectangle; don't make new drawing.
                self.draw_shape()

    def set_height(self,new_height):
        """
        Change the height of the rectangle.

        :param new_height: height (vertical dimension) of rectangle.  Must be >= 0.  Otherwise, no change is made.
        """   
        if new_height>=0 :
            self.height=new_height
            self.length=new_height
            if self.has_been_drawn : #Only redraw rectangle; don't make new drawing.
                self.draw_shape()
    
