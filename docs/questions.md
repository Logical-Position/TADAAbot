# Questions

## For Production
* Authentication -- who are we walling out and how?
    * ADFS account
    * Email + password
    * Google account
    * Different permission levels?
    * Verify @logicalposition.com email address
* How will the database be hosted?
    * Planetscale is an option.
    * If internal resources can create a managed db somewhere, like AWS 
* How will the web-app be hosted?
    * Possibly internally on something like AWS
    * Google Hosting
* What is our MVP (minimum viable product) and how are we defining it?
    * What bugs remain in the code that prevent this from going to production?
    * What features are missing that are needed for production?


## For Testing
* How do we want to receive feedback?
    * Google Forms
* Powerpoint general questions
    * Direct feedback on manual input options
    * What else would you like to change?
    * Any desired formatting changes to the powerpoint?
* How we testing / ensuring PPTs are correct?
    * I think this initial testing period should be internal only -- no documents sent outside of LP


## For Clients
* Discuss options for final hosting.
    * Pricing considerations (it can possibly be free, we'll see in testing)
    * Maintaince access
* What are management's wishes for security / access control?
    * Does it need to be walled from the public?
    * Who should have permission to submit audits?


## For Development
* What types of logs should we keep?
* How should we structure receiving feedback from testers?
    * What feedback are we specifically looking for, if any?
    * Should we create any specific channels for testers to submit feedback? Perhaps like an email link on the application itself.
    * Where and how should we compile this feedback?
* What is the line between 0.0 and 0.1? 
    * I think we'll retroactively define a commit as '0.0'. After this, we'll have more to talk about in regards to what 0.1 is (but 0.1 will also probably be tagged retroactively).