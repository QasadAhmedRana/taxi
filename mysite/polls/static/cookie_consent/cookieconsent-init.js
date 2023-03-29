// obtain cookieconsent plugin
var cc = initCookieConsent();

// example logo
var logo = '<img src="https://img1.wsimg.com/isteam/ip/2bcc904d-c449-4d1b-893d-fdd48f717df3/blob-0025.png/:/cr=t:12.41%25,l:0%25,w:100%25,h:75.19%25/rs=w:800,h:602,cg:true" alt="Logo" loading="lazy" style="margin-left: -4px; margin-bottom: -5px; height: 35px">';
var cookie = '🍪';

// run plugin with config object
cc.run({

    current_lang : 'de',
    autoclear_cookies : true,                   // default: false
    cookie_name: 'cc_cookie_demo1',             // default: 'cc_cookie'
    cookie_expiration : 365,                    // default: 182
    page_scripts: true,                         // default: false

    // auto_language: null,                     // default: null; could also be 'browser' or 'document'
    // autorun: true,                           // default: true
    // delay: 0,                                // default: 0
    force_consent: true,
    hide_from_bots: true,                   // default: false
    // remove_cookie_tables: false              // default: false
    // cookie_domain: location.hostname,        // default: current domain
    // cookie_path: "/",                        // default: root
    // cookie_same_site: "Lax",
    // use_rfc_cookie: false,                   // default: false
    // revision: 0,                             // default: 0

    gui_options: {
        consent_modal: {
            layout: 'box',                      // box,cloud,bar
            position: 'bottom right',           // bottom,middle,top + left,right,center
            transition: 'slide'                 // zoom,slide
        },
        settings_modal: {
            layout: 'box',                      // box,bar
            // position: 'left',                // right,left (available only if bar layout selected)
            transition: 'slide'                 // zoom,slide
        }
    },

    onFirstAction: function(){
        console.log('onFirstAction fired');
    },

    onAccept: function (cookie) {
        console.log('onAccept fired ...');
    },

    onChange: function (cookie, changed_preferences) {
        console.log('onChange fired ...');
    },

    languages: {
        'en': {
            consent_modal: {
                title: cookie + ' Wir verwenden cookies! ',
                description: 'Hi, Wir verwenden Cookies, um sicherzustellen, dass wir Ihnen die beste Erfahrung auf unserer Website bieten. Einige dieser Cookies sind unbedingt erforderlich, während andere uns helfen, Ihre Erfahrung zu verbessern, indem sie Einblicke darüber geben, wie die Website genutzt wird. Wenn Sie auf "Akzeptieren" klicken, stimmen Sie der Verwendung aller Cookies zu. Wenn Sie auf <button type="button" data-cc="c-settings" class="cc-link">Einstellungen</button> klicken, können Sie jedoch eine kontrollierte Zustimmung geben. ',
                primary_btn: {
                    text: 'Alle akzeptieren',
                    role: 'accept_all'              // 'accept_selected' or 'accept_all'
                },
                secondary_btn: {
                    text: 'Nur Essenzielle',
                    role: 'accept_necessary'        // 'settings' or 'accept_necessary'
                }
            },
            settings_modal: {
                title: logo,
                save_settings_btn: 'Einstelllungen Speichern',
                accept_all_btn: 'Alle akzeptieren',
                reject_all_btn: 'Nur Essenzielle',
                close_btn_label: 'Schließen',
                cookie_table_headers: [
                    {col1: 'Name'},
                    {col2: 'Domain'},
                    {col3: 'Expiration'},
                    {col4: 'Description'}
                ],
                blocks: [
                    {
                        title: 'Verwendung von Cookies 📢',
                        description: 'Wir verwenden Cookies, um sicherzustellen, dass wir Ihnen die beste Erfahrung auf unserer Website bieten. Wenn Sie diese Website weiterhin nutzen, gehen wir davon aus, dass Sie damit einverstanden sind. Weitere Details zur Cookies Verwendung entnehmen Sie bitte unser <a href="#" class="cc-link">Datenschutzerklärung</a>.'
                    }, {
                        title: 'Essenzielle Cookies',
                        description: 'Diese Website verwendet Cookies, um Ihre Erfahrung zu verbessern, während Sie durch die Website navigieren. Von diesen Cookies werden die als notwendig kategorisierten Cookies in Ihrem Browser gespeichert, da sie für das Funktionieren der grundlegenden Funktionen der Website unerlässlich sind.',
                        toggle: {
                            value: 'necessary',
                            enabled: true,
                            readonly: true          // cookie categories with readonly=true are all treated as "necessary cookies"
                        }
                    }, {
                        title: 'Performance and Analytics cookies',
                        description: '',
                        toggle: {
                            value: 'analytics',     // there are no default categories => you specify them
                            enabled: false,
                            readonly: false
                        },
                        cookie_table: [
                        /*
                            {
                                col1: '^_ga',
                                col2: 'google.com',
                                col3: '2 years',
                                col4: 'description ...',
                                is_regex: true
                            },
                            {
                                col1: '_gid',
                                col2: 'google.com',
                                col3: '1 day',
                                col4: 'description ...',
                            }
                            */
                        ]
                    }, {
                        title: 'Gezielte Werbung Cookies',
                        description: 'Wir verwenden Cookies, um Ihnen das bestmögliche Erlebnis zu bieten. Einige Cookies sind für den Betrieb unseres Websites unbedingt erforderlich, während andere uns helfen, Ihre Einstellungen, Analysen und Marketing-Aktivitäten zu speichern. Wenn Sie auf unserer Website surfen, stimmen Sie der Verwendung dieser Cookies zu. Sie können Ihre Cookie-Einstellungen jedoch jederzeit ändern.',
                        toggle: {
                            value: 'targeting',
                            enabled: false,
                            readonly: false
                        }
                    }, {
                        title: 'Weitere Informationen',
                        description: 'Für weitere Fragen über Cookies und Datenschutzerklärung oder <a class="cc-link" href="https://iftaxi.de/kontakt">kontaktieren</a>  Sie uns.',
                    }
                ]
            }
        }
    }

});