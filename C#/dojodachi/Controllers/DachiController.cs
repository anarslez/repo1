using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.DependencyInjection;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using dojodachi.Models;
namespace dojodachi.Controllers     //be sure to use your own project's namespace!
{
    // Somewhere in your namespace, outside other classes
    public static class SessionExtensions
    {
        // We can call ".SetObjectAsJson" just like our other session set methods, by passing a key and a value
        public static void SetObjectAsJson(this ISession session, string key, object value)
        {
            // This helper function simply serializes theobject to JSON and stores it as a string in session
            session.SetString(key, JsonConvert.SerializeObject(value));
        }

        // generic type T is a stand-in indicating that we need to specify the type on retrieval
        public static T GetObjectFromJson<T>(this ISession session, string key)
        {
            string value = session.GetString(key);
            // Upon retrieval the object is deserialized based on the type we specified
            return value == null ? default(T) : JsonConvert.DeserializeObject<T>(value);
        }
    }
    public class DachiController : Controller   //remember inheritance??
    {
        //for each route this controller is to handle:
        [HttpGet]       //type of request
        [Route("")]     //associated route string (exclude the leading /)
        public IActionResult Index()
        {
            Dachi mypet = HttpContext.Session.GetObjectFromJson<Dachi>("DachiData");
            if (mypet == null)
            {
                HttpContext.Session.SetObjectAsJson("DachiData", new Dachi());
            }
            ViewBag.DachiData = HttpContext.Session.GetObjectFromJson<Dachi>("DachiData");
            if (ViewBag.DachiData.fullness < 1 || ViewBag.DachiData.happiness < 1)
            {
                ViewBag.DachiData.status = "Your Dachi just died...";
            }
            if (ViewBag.DachiData.fullness > 100 && ViewBag.DachiData.happiness > 100 && ViewBag.DachiData.energy > 100)
            {
                ViewBag.DachiData.status = "You won!";
            }
            return View("Index");
        }
        [HttpPost]
        [Route("Restart")]
        public IActionResult Reset()
        {
            HttpContext.Session.Clear();
            return RedirectToAction("Index");
        }
        [HttpPost]
        [Route("Feed")]
        public IActionResult Feed()
        {
            Dachi CurrDachiData = HttpContext.Session.GetObjectFromJson<Dachi>("DachiData");
            if(CurrDachiData.meals > 0){
                CurrDachiData.feed();
            } else {
                CurrDachiData.status = "No Meals... your Dachi cannot eat. Work to earn meals.";
            }
            HttpContext.Session.SetObjectAsJson("DachiData",CurrDachiData);
            return RedirectToAction("Index");
        }
        [HttpPost]
        [Route("Play")]
        public IActionResult Play()
        {
            Dachi CurrDachiData = HttpContext.Session.GetObjectFromJson<Dachi>("DachiData");
            if(CurrDachiData.energy > 0){
                CurrDachiData.play();
            } else {
                CurrDachiData.status = "No Energy... your Dachi cannot play.";
            }
            HttpContext.Session.SetObjectAsJson("DachiData",CurrDachiData);
            return RedirectToAction("Index");
        }
        [HttpPost]
        [Route("Work")]
        public IActionResult Work()
        {
            Dachi CurrDachiData = HttpContext.Session.GetObjectFromJson<Dachi>("DachiData");
            if(CurrDachiData.energy > 0){
                CurrDachiData.work();
            } else {
                CurrDachiData.status = "No Energy... your Dachi cannot work.";
            }
            HttpContext.Session.SetObjectAsJson("DachiData",CurrDachiData);
            return RedirectToAction("Index");
        }
        [HttpPost]
        [Route("Sleep")]
        public IActionResult Sleep()
        {
            Dachi CurrDachiData = HttpContext.Session.GetObjectFromJson<Dachi>("DachiData");
            CurrDachiData.sleep();
            HttpContext.Session.SetObjectAsJson("DachiData",CurrDachiData);
            return RedirectToAction("Index");
        }
    }
}