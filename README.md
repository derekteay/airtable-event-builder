# airtable-event-builder
Using the AirTable API and Python, build a PHP array for a list of given events

This project uses the AirTable Python Wrapper - https://github.com/gtalarico/airtable-python-wrapper

# Output
Here is the following PHP output:

```
<?php
$content = array(
	"kiel" => array(
		array(
			"title" => "Healthcare Hackathon - Kiel - 09/13/2018",
			"date" => "13/Sep/2018",
			"display_city" => "Kiel",
			"url" => "https://www.healthcare-hackathon.eu/hackathon-14-15-9/",
			"desc" => "The Healthcare Hackathon is for everyone who is interested in health and technology. This unique event combines teamwork, interactive workshops, highly trained specialists and a great public event. Attend the IBM Worshops to learn about AI and Blockchain. Take what you learn at these events and apply it to these three challenge areas: 1. Financial networks built on blockchain technology can improve the distribution of aid before and after a major disaster, 2. Tools that can translate and convert speech to text and vice versa can improve how fast people are warned and assisted, 3. Understanding the healthcare needs of populations in advance can improve their resistance to threats to their health.Get started with the code patterns at http://ibm.biz/C4CHealthcare",
			"addr" => "Sparkassen-Arena-Kiel Europaplatz 124103 Kiel Germany",
		)
	),
	"new-york-city" => array(
		array(
			"title" => "Columbia Call for Code Hackathon",
			"date" => "15/Sep/2018",
			"display_city" => "New York City",
			"url" => "",
			"desc" => "A day to learn how to use IBM Cloud technology and leverage it for your Call For Code ideas. We'll teach you everything you need to know so you can submit your idea and help to prevent, mitigate, or rebuild after natural disasters.",
			"addr" => "",
		),
		array(
			"title" => "United Nations Call for Code Workshop",
			"date" => "13/Sep/2018",
			"display_city" => "New York City",
			"url" => "",
			"desc" => "A day to learn how to use IBM Cloud technology and leverage it for your Call For Code ideas. We'll teach you everything you need to know so you can submit your idea and help to prevent, mitigate, or rebuild after natural disasters.",
			"addr" => "",
		)
	),
	"virtual" => array(
		array(
			"title" => "Virtual Call for Code Hackathon",
			"date" => "14/Sep/2018",
			"display_city" => "Virtual",
			"url" => "",
			"desc" => "A day to learn how to use IBM Cloud technology and leverage it for your Call For Code ideas. We'll teach you everything you need to know so you can submit your idea and help to prevent, mitigate, or rebuild after natural disasters.",
			"addr" => "",
		)
	)
);
```

