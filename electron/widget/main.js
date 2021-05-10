console.log('main process working');
console.log('main.js');



const electron = require("electron");
const app = electron.app;

const  BrowserWindow = electron.BrowserWindow;
const path = require("path");
const url = require("url");


let win;
function createWindow(){
  var screenElectron = electron.screen;
  var mainScreen = screenElectron.getPrimaryDisplay();
  var dimensions = mainScreen.size;
    win = new BrowserWindow({
      
      skipTaskbar:true,
      transparent:true,
        frame:false,
        alwaysOnTop:true,
        titleBarStyle: 'hidden',
        width :dimensions.width+55,
        height : dimensions.height+55,
      
        webPreferences: {
          contextIsolation: true
        }
      });
    win.removeMenu();
    win.loadURL(url.format({
        pathname: path.join(__dirname,"widget/index.html"),
        protocol:"file",
        slashes:true
    }
    ));
      //  win.webContents.openDevTools();
    win.on('closed',()=> {
        win = null;
    })
}
app.on('ready',createWindow);