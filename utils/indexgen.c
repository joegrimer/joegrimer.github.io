#include <stdio.h> 
#include <dirent.h> 
#include <string.h> 
#include <sys/stat.h>

void do_dir(char *path, int level) 
{ 
   struct dirent *de;  // Pointer for directory entry 
   char file_name[1024];

   // opendir() returns a pointer of DIR type.  
   DIR *dr = opendir(path); 

   if (dr == NULL)  // opendir returns NULL if couldn't open directory 
   { 
      printf("Could not open current directory" ); 
      return; 
   } 

   struct stat stbuf;
   while ((de = readdir(dr)) != NULL) {
      strcpy(file_name, de->d_name);
      if (file_name[0] == *".") continue;
      char full_file_name[1024];
    strcpy(full_file_name, path);
    strcat(full_file_name, "/");
    strcat(full_file_name, file_name);
      
      stat(full_file_name, &stbuf); // livin on the edge
      printf("<p>");
      for(int i=0;i<level;i++) printf("&nbsp;&nbsp;&nbsp;");
      if ((stbuf.st_mode & S_IFMT) == S_IFDIR) {
          printf("%s/</p>\n", file_name);
          char sub_file_name[1024];
          strcpy(sub_file_name, path);
          strcat(sub_file_name, "/");
          strcat(sub_file_name, file_name);
          do_dir(sub_file_name, level+1);
      } else {
          printf("<a href='%s/%s'>%s</a></p>\n", path, file_name, file_name);
      }
   }
  
   closedir(dr);   
   return; 
}

int main(void) 
{ 
   printf("<!doctype html><html><head><link rel='stylesheet' href='style.css' /><title>Hello There!</title><body>");
   printf("An inelegant dump of everything on this git repository");
   do_dir(".", 0);
   printf("</body></html>");
} 
