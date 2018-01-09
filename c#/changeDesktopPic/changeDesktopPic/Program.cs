using System;
using System.Collections.Generic;
using System.Configuration;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace changeDesktopPic
{
    class Program
    {
        static void Main(string[] args)
        {
            string baseDir = ConfigurationManager.AppSettings["PicPath"];
            FileInfo[] picFiles = new DirectoryInfo(baseDir).GetFiles();

            Random rand = new Random(DateTime.Now.GetHashCode());
            int chooseIndex = rand.Next(picFiles.Length);
            FileInfo pic = picFiles[chooseIndex];

            Wallpaper.Set(new Uri(pic.FullName), Wallpaper.Style.Stretched);
        }
    }
}
