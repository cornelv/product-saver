const puppeteer = require('puppeteer-core');
const fs = require('fs').promises;

/*
var options = {
  width: 300,
  height: 600,
};
*/

async function sleep(millis) {
  return new Promise(resolve => setTimeout(resolve, millis));
}

let results = [['tag', 'posts']];

(async () => {

  const jquery_content = await fs.readFile('utils/jquery.js', "utf8");

  let data = await fs.readFile('utils/tags_list.txt', "utf8"); // need to be in an async function
  
  data = data.replace(/\n/g, "");
  data = data.replace(/ /g,'');
  data = data.split("#");

  data = [...new Set(data)];

  // parte the hashtags

  const browser = await puppeteer.launch({
    "executablePath": "/usr/bin/chromium-browser", 
    headless: false
    // args: [`--window-size=${options.width},${options.height}`]
  });
  const page = await browser.newPage();

  // for each hash tag go to the page

  let idx = 0;
  for(let tag of data){

      if(tag == ''){
        continue;
      }

      await page.goto('https://www.instagram.com/explore/tags/'+ tag, {waitUntil: 'networkidle2'});
      
      try{
        await page.addScriptTag({content: jquery_content});  
      }
      catch(err){
        console.log(err);
      }
      
    
      let posts = await page.evaluate(() => {
        const $ = window.$; //otherwise the transpiler will rename it and won't work
        return $('.-nal3').text();
      });

      posts = posts.replace(" posts", "");
      posts = posts.replace(/,/g, "");

      results.push([tag, posts]);

      console.log("finished this tag "+ tag +" left: ", data.length - idx);

      await sleep(5* 1000);

      idx++;
  }

  browser.close();

  await fs.writeFile('utils/results.txt', JSON.stringify(results));

  //console.log(results);

})();