using System.ComponentModel.DataAnnotations;
namespace dojosurvey.Models
    {
        public class Response
    	{
            [Required]
            [EmailAddress]
            public string email {get;set;}
            [Required]
            public string loc {get;set;}
            [Required]
            public string lang {get;set;}
            [Required]
            [MinLength(10)]
            public string com {get;set;}

    	}
        
    }