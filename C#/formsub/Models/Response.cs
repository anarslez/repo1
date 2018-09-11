using System.ComponentModel.DataAnnotations;
namespace formsub.Models
    {
        public class Response
    	{
            [Required]
            [MinLength(4)]
            public string fname { get; set; }

            [Required]
            [MinLength(4)]
            public string lname { get; set; }

            [Required]
            [Range(0,200)]
            public int age { get; set; }

            [Required]
            [EmailAddress]
            public string email {get;set;}

            [Required]
            [MinLength(8)]
            public string password {get;set;}

    	}
        
    }