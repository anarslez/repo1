using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
namespace razorfun.Controllers     //be sure to use your own project's namespace!
{
    public class RazorController : Controller   //remember inheritance??
    {
        //for each route this controller is to handle:
        [HttpGet]       //type of request
        [Route("")]     //associated route string (exclude the leading /)
        public IActionResult Index()
        {
            return View("Index");
        }
    }
}