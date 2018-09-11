using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
namespace portfolio.Controllers     //be sure to use your own project's namespace!
{
    public class PortfolioController : Controller   //remember inheritance??
    {
        //for each route this controller is to handle:
        [HttpGet]       //type of request
        [Route("")]     //associated route string (exclude the leading /)
        public IActionResult Index()
        {
            return View("Index");
        }
        [HttpGet]       //type of request
        [Route("projects")]     //associated route string (exclude the leading /)
        public IActionResult Project()
        {
            return View("Project");
        }
        [HttpGet]       //type of request
        [Route("contact")]     //associated route string (exclude the leading /)
        public IActionResult Contact()
        {
            return View("Contact");
        }
    }
}