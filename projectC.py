import math
import VTK_mesh_proc

class Surface:
    def __init__(self,filename):
        [self.faceList, self.vertexList, self.vtkData] = VTK_mesh_proc.read_VTK_withScales(filename)


    def display(self, scalers=[], scalarsOnFaces=True):
        """
        Displays surface
        """
        if scalers != []:
            vtkData = VTK_mesh_proc.addScalers(self.vtkData, self.triangleAreaList(), scalarsOnFaces)
        else:
            vtkData = self.vtkData
        VTK_mesh_proc.render(vtkData)
        
    def numVertices(self):
        """
        This method returns the number of vertices that are present in the triangulated 
        surface of the right hippocampus. The number of vertices are determined by using 
        the len() function on self.vertexList which will return how many elements (vertices)
        are in the list.
        """
        
        totalvertices = len(self.vertexList)
        
        return totalvertices
    
    def numFaces(self):
        """
        This method returns the number of triangular faces that are present in the 
        triangulated surface of the right hippocampus. The number of faces are 
        determined by using the len() function on self.faceList which will return 
        how many elements (faces) are in the list.
        """    
        
        totalfaces = len(self.faceList)
        
        return totalfaces
        
    def triangleArea(self, vertices):    
        """
        This method returns the area of a triangle when given its three vertices. 
        Heron's formula is used to calculate the area. 
        """
        self.vertices = vertices
        a = math.sqrt((self.vertices[1][0] - self.vertices[0][0])**2 + (self.vertices[1][1] - self.vertices[0][1])**2 + (self.vertices[1][2] - self.vertices[0][2])**2)
        b = math.sqrt((self.vertices[2][0] - self.vertices[0][0])**2 + (self.vertices[2][1] - self.vertices[0][1])**2 + (self.vertices[2][2] - self.vertices[0][2])**2)
        c = math.sqrt((self.vertices[2][0] - self.vertices[1][0])**2 + (self.vertices[2][1] - self.vertices[1][1])**2 + (self.vertices[2][2] - self.vertices[1][2])**2)
        d = (a + b + c) / 2
        
        area = math.sqrt(d * (d - a) * (d - b) * (d - c))
        
        return area
        

    def triangleVolume(self, vertices):    
        """
        This method returns the volume of a triangle when given its three vertices. 
        This is done by calculating the volume of a tetrahedral which goes from the
        origin to the triangles vertices. Note that the sign of the volume depends
        on the face orientation of the triangle.
        """
        self.vertices = vertices
        
        volume = (1/6)*((self.vertices[0][1]*self.vertices[1][2] - self.vertices[0][2]*self.vertices[1][1])*(self.vertices[2][0])
                       + (self.vertices[0][2]*self.vertices[1][0] - self.vertices[0][0]*self.vertices[1][2])*(self.vertices[2][1])
                       + (self.vertices[0][0]*self.vertices[1][1] - self.vertices[0][1]*self.vertices[1][0])*(self.vertices[2][2]))
        
        return volume
        
        
    def triangleAreaList(self):
        """
        This method returns all the areas of each triangle in a list. This is 
        done by looping through the faceList which is a list that contains list.
        The sub list contains the index that belongs to a position in the vertex
        list. 
        """
        self.list1 = []
        for i in self.faceList:
            a = [self.vertexList[i[0]], self.vertexList[i[1]], self.vertexList[i[2]]]
            b = Surface.triangleArea(self, a)
            self.list1.append(b)
        
        return self.list1
    
        
    def area(self):
        """
        This method returns the surface area of the triangulated surface. 
        This is done by first calling the triangleAreaList method which
        returns a list with all the areas of each triangle. Then, the
        sum function is used to get the surface area.
        """
        a = Surface.triangleAreaList(self)
        
        return sum(a)
        
    
    def volume(self):
        """
        This method returns the total volume of the triangulated surface. The
        total volume is calculated by looping through the faceList to get vertices.
        These vertices are then used as an argument for the triangleVolume method.
        Each volume output from that method is then appended to a list. Then, the sum
        function is used to add up all the volumes.
        """
        self.list2 = []
        for i in self.faceList:
            a = [self.vertexList[i[0]], self.vertexList[i[1]], self.vertexList[i[2]]]
            b = Surface.triangleVolume(self, a)
            self.list2.append(b)
            
        return sum(self.list2)
        
        

def main():
    name = 'rightHippocampus.vtk'   
    S = Surface(name)
    
    S.display(S.triangleAreaList())
    print('The surface area and volume are {:.2f} mm^2 and {:.2f} mm^3 respectively.' .format(S.area(), S.volume()))
    
    
if __name__ == "__main__": main()    