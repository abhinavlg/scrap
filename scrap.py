from playwright.sync_api import sync_playwright


def get_full_page_content(url):
    with sync_playwright() as p:
        # Launch browser in headless mode
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Navigate to the URL
        page.goto(url)
        
        # Extract full HTML
        full_html = page.content()
        
        # Extract all elements (equivalent to inspect element)
        elements_info = page.evaluate("""() => {
            // Function to recursively extract element details
            function getElementDetails(element) {
                if (!element) return null;
                
                // Basic element information
                const details = {
                    tagName: element.tagName,
                    attributes: {},
                    textContent: element.textContent.trim(),
                    innerHTML: element.innerHTML,
                    outerHTML: element.outerHTML
                };
                
                // Collect all attributes
                for (let attr of element.attributes) {
                    details.attributes[attr.name] = attr.value;
                }
                
                // Collect computed styles
                const computedStyles = window.getComputedStyle(element);
                details.computedStyles = {};
                for (let prop of computedStyles) {
                    details.computedStyles[prop] = computedStyles.getPropertyValue(prop);
                }
                
                // Recursively get child elements
                details.children = Array.from(element.children).map(getElementDetails);
                
                return details;
            }
            
            // Get the entire document as a structured object
            return getElementDetails(document.documentElement);
        }""")
        
        # Close the browser
        browser.close()
        
        return {
            'full_html': full_html,
            'elements_info': elements_info
        }

