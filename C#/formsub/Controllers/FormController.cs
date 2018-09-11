using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using formsub.Models;
namespace formsub.Controllers     //be sure to use your own project's namespace!
{
    public class FormController : Controller   //remember inheritance??
    {
        //for each route this controller is to handle:
        [HttpGet]       //type of request
        [Route("")]     //associated route string (exclude the leading /)
        public IActionResult Index()
        {
            return View("Index");
        }
        [HttpPost]
        [Route("method")]
        public IActionResult Method(Response newresponse)
        {
            if (ModelState.IsValid)
            {
                // do somethng!  maybe insert into db?  then we will redirect
                return View("Show", newresponse);
            }
            else
            {
                // Oh no!  We need to return a ViewResponse to preserve the ModelState, and the errors it now contains!
                return View("Index");
            }
        }
    }
}