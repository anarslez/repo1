using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using viewmodel.Models;
namespace viewmodel.Controllers     //be sure to use your own project's namespace!
{
    public class ModelController : Controller   //remember inheritance??
    {
        //for each route this controller is to handle:
        [HttpGet]       //type of request
        [Route("")]     //associated route string (exclude the leading /)
        public IActionResult Index()
        {
            Message mess = new Message()
            {mess = "kdsfkdljfljslkfjksdjdf whoaaaaaaaaaaa dfdkslk"};
            return View("Index", mess);
        }
        [HttpGet]       //type of request
        [Route("name")]
        public IActionResult Names()
        {
            Name names = new Name() 
            {nam = new string[] {"Sally", "Billy", "Joey", "Moose"}
            };
            return View("Names", names);
        }
        [HttpGet]       //type of request
        [Route("number")]
        public IActionResult Numbers()
        {
            Number nums = new Number() 
            {num = new int[] {1,2,3,4}
            };
            return View("Numbers", nums);
        }
    }
}