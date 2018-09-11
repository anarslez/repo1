using Microsoft.AspNetCore.Mvc;
using System.Linq;
using DbConnection;
using Microsoft.AspNetCore.Http;
using System;

namespace quotedojo {
    public class QuoteController : Controller {
        [HttpGet]
        [Route("")]
        public IActionResult Index() {
            if(TempData["Error"] != null){
                ViewBag.Error = TempData["Error"];
            }
            return View();
        }

        [HttpPost]
        [Route("quotes")]
        public IActionResult Create(string name, string quote){
            if(name == "" || quote == ""){
                TempData["Error"] = "Neither field should be empty!";
                return RedirectToAction("Index");
            }
            //Add the quote to the database
            string query = $"INSERT INTO quotes (quote, name, created_at, updated_at) VALUES ('{quote}', '{name}', NOW(), NOW());";
            DbConnector.Execute(query);
            return RedirectToAction("Quotes");    
        }

        [HttpGet]
        [Route("quotes")]
        public IActionResult Quotes(){
            //Get all quotes
            // string query = "SELECT * FROM quotes";
            // var quotes = DbConnector.Query(query);
            // ViewBag.Quotes = quotes;
            return View();
        }
    }
}
