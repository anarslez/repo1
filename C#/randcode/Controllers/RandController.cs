using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using randcode.Models;
using System;
namespace randcode.Controllers     //be sure to use your own project's namespace!
{
    public class RandController : Controller   //remember inheritance??
    {
        //for each route this controller is to handle:
        [HttpGet]       //type of request
        [Route("")]     //associated route string (exclude the leading /)
        public IActionResult Index()
        {
            if (TempData["rand"] != null)
            {
                TempData["rand"] = "not random";
            }
            else
            {
                var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
                var stringChars = new char[14];
                var random = new Random();

                for (int i = 0; i < stringChars.Length; i++)
                {
                    stringChars[i] = chars[random.Next(chars.Length)];
                }

                var finalString = new String(stringChars);
                TempData["rand"] = finalString;
            }
            return View("Index", TempData);
        }
        
    }
}