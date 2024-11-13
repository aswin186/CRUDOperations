from django.db import models

# <label for="title">Title</label>
#     <input type="text" name="title">
#     <br>
#     <label for="description">Description</label>
#     <input type="text" name="description">
#     <br>
#     <label for="poster">Image</label>
#     <input type="file" name="poster">
#     <br>
#     <label for="status">Status</label>
#     <select name="status" id="dropdown">
#         <option value="Pending">Pending</option>
#         <option value="In_Progress">In Progress</option>
#         <option value="Completed">Completed</option>
#     </select>

class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=150)
    status = models.CharField(max_length=50)
    poster = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title +"-----"+ self.status +"-----"+ str(self.created_at)