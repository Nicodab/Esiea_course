use reqwest;
use scraper::{Html, Selector};
fn main() -> Result<(), reqwest::Error> {
    let url: &str = "http://httpforever.com";

    let body: String = reqwest::blocking::get(url)?.text()?; // Blocking pour éviter de faire de l'asynchrone
    let document = Html::parse_document(&body); // & car il prend pas une String mais un str
    let selector = Selector::parse("a[href]").unwrap();
    
    for link in document.select(&selector) {
        let href = link.value().attr("href").unwrap_or("");
    
        if href.contains("facebook") || href.contains("twitter") || href.contains("linkedin") {
            println!("{}", href);
        }
    }
    Ok(())
}
