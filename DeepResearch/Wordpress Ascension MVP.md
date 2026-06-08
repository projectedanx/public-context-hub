{  
  "WordPressAscensionMVP": {  
    "description": "A specification for the Minimum Viable Product (MVP) to validate the core hypothesis of AI-agent co-operation with a deconstructed WordPress backend. This MVP focuses on the smallest set of testable modules for sandboxing, execution, and traceability.",  
    "SandboxingModules":, we eliminate entire classes of vulnerabilities and unpredictable behaviors tied to the legacy request-response lifecycle.\[2, 3\] This forces the AI agent to interact with a constrained, explicit, and purely programmatic surface, which is a prerequisite for safe and testable operations."  
      },  
      {  
        "component": "Simplified Content Model",  
        "description": "Utilization of the standard \`wp\_posts\` table but with interaction logic that enforces content as structured data. For the MVP, this is simplified to two fields: \`title\` (string) and \`content\` (plain text). The API will reject any raw HTML or shortcode-like syntax in the content field.",  
        "causal\_justification": "This module tests the hypothesis that an AI can operate on structured data rather than ambiguous HTML blobs.\[1\] By simplifying the content model and explicitly forbidding embedded logic like shortcodes (which are notoriously problematic in headless environments \[4, 5, 6\]), we create a controllable proof point for data manipulation and prevent the agent from triggering unintended side effects."  
      }  
    \],  
    "ExecutionModules": This module is the minimum viable implementation for identifying and authorizing an agent, ensuring that every action can be attributed to a specific, authenticated principal."  
      },  
      {  
        "component": "Atomic Content Primitives",  
        "description": "A minimal set of RESTful API endpoints representing the core content lifecycle: \`POST /nodes\` (to create a draft), \`PATCH /nodes/{id}\` (to update content), and \`GET /nodes/{id}\` (to retrieve content). These primitives are designed to be simple, single-purpose, and chainable.",  
        "causal\_justification": "LLM-based agents operate most reliably when executing a sequence of simple, atomic steps rather than constructing a single, complex command.\[9\] These primitives provide a bounded set of actions that reduce the agent's cognitive load and minimize the risk of hallucinating incorrect parameters, directly testing the feasibility of modular, step-wise operation.\[10\]"  
      },  
      {  
        "component": "Simplified Semantic Affordances",  
        "description": "API responses for \`GET /nodes/{id}\` will include a \`\_links\` object containing a list of possible actions (e.g., \`update\`, \`request\_publication\`) with their corresponding API endpoints and HTTP methods. This provides the agent with a machine-readable menu of valid next steps based on the resource's current state.",  
        "causal\_justification": "This is a core test of co-agency. Instead of forcing the agent to infer possible actions, the API explicitly communicates what can be done next.\[11, 12\] This reduces ambiguity and prevents errors by making the API self-describing.\[13, 12\] This MVP implementation validates that an agent can interpret and use these affordances to navigate the application's state machine reliably, a key principle for robust machine clients.\[14\]"  
      }  
    \],  
    "TraceabilityModules": By forcing the agent to request approval, we test the hypothesis that it can operate as a supervised assistant within defined boundaries, with all irreversible actions being auditable and explicitly authorized by a human.\[16, 17\]"  
      },  
      {  
        "component": "Immutable Action Log",  
        "description": "A simple, append-only logging mechanism (e.g., writing to a dedicated log file or database table). Every API call initiated by the agent is recorded with the agent's ID, the action performed, the target resource, and a timestamp.",  
        "causal\_justification": "Traceability is fundamental to accountability. This module creates an immutable audit trail of every action the agent takes. This log is the ground truth for debugging agent behavior, verifying that it adheres to its instructions, and providing a complete, verifiable history of its operations for post-hoc analysis."  
      }  
    \]  
  }  
}

Here are the technical specifications for the Sandboxing Modules of the WordPress Ascension MVP.

### **Module 1: Presentation Layer Retirement**

This module ensures the WordPress backend is completely isolated from any frontend rendering, establishing it as a pure, API-first data source. All non-API and non-admin requests will be programmatically terminated, preventing the theme engine from ever being invoked.

#### **Technical Tasks**

1. **Implement a Global Redirect Hook:** A function must be created that hooks into WordPress's `template_redirect` action. This hook is chosen because it fires before any template files are loaded for a frontend request, making it the ideal point for interception.    
2. **Develop Request Analysis Logic:** Inside the hooked function, logic must be implemented to analyze the incoming request URI. The function must differentiate between three types of requests:  
   * **Frontend Requests:** Any request that is not for `/wp-admin/` or `/wp-json/`. These are the targets for redirection.  
   * **Admin Area Requests:** Requests to `/wp-admin/` must be allowed to pass through unmodified to retain administrative access for human operators.  
   * **API Requests:** Requests to `/wp-json/` (the REST API) or `/graphql` (if applicable) must be allowed to pass through unmodified.  
3. **Execute Redirection or Termination:** For any request identified as a frontend request, the function will not perform a standard redirect. Instead, it will directly issue an HTTP `404 Not Found` response and terminate the script. This provides a clear, machine-readable signal that the requested resource (a webpage) does not exist in this paradigm.

#### **API Contract (System Behavior)**

This contract defines the expected system response for any non-API, non-admin HTTP request.

* **Endpoint:** Any frontend URL (e.g., `GET /`, `GET /sample-post/`, `GET /category/news/`)  
* **Method:** `GET`  
* **Expected Behavior:** The system intercepts the request before the theme engine is engaged.  
* **Success Response (Not Applicable):** No frontend page is ever served.  
* **Error/Termination Response:**  
  * **Status Code:** `404 Not Found`

**Response Body (JSON):**  
JSON  
{  
  "code": "ascension\_frontend\_retired",  
  "message": "The presentation layer is disabled. Access is available only via the designated API endpoints.",  
  "data": {  
    "status": 404  
  }  
}

* 

### **Module 2: Simplified Content Model**

This module establishes a strict, machine-friendly content structure. It redefines the core content fields and implements validation at the API level to reject unstructured data like HTML and shortcodes, which are common failure points in headless environments.  

#### **Technical Tasks**

1. **Register Custom REST API Fields:** Use the `register_rest_field` function to expose two specific fields for the `post` type: `title` and `content`.  
2. **Implement Strict Validation Callbacks:** For the `content` field, a `validate_callback` function must be implemented. This callback will perform two checks:    
   * **HTML Detection:** It will compare the submitted string against the same string with `strip_tags()` applied. If they are not identical, it signifies the presence of HTML, and the validation fails.  
   * **Shortcode Detection:** It will use a regular expression to check for the presence of the `[...]` shortcode pattern. If a match is found, the validation fails.  
3. **Return `WP_Error` on Validation Failure:** If the validation callback fails, it must return a `WP_Error` object. This ensures the API responds with a proper error code and message, providing clear feedback to the AI agent.

#### **API Contract**

This contract defines the endpoints for creating and updating a content node, enforcing the simplified model.

**Endpoint: `POST /wp-json/wp/v2/posts`**

* **Method:** `POST`  
* **Description:** Creates a new content node.

**Request Body (JSON):**  
JSON  
{  
  "title": "A Valid Node Title",  
  "content": "This is a simple, plain text paragraph. It contains no HTML or shortcodes.",  
  "status": "draft"  
}

*   
* **Validation Rules:**  
  * `title`: Must be a string.  
  * `content`: Must be a plain text string. The API will reject the request if it contains any HTML tags (e.g., `<p>`, `<strong>`) or shortcode patterns (e.g., `[gallery]`).  
* **Success Response:**  
  * **Status Code:** `201 Created`  
  * **Response Body:** A JSON object representing the newly created post, including its ID, title, and plain text content.  
* **Error Response (Validation Failure):**  
  * **Status Code:** `400 Bad Request`

**Response Body (JSON):**  
JSON  
{  
  "code": "rest\_invalid\_param",  
  "message": "Invalid parameter(s): content",  
  "data": {  
    "status": 400,  
    "params": {  
      "content": "Content must be plain text and cannot contain HTML or shortcodes."  
    }  
  }

* }

Here are the technical specifications for the Execution Modules, designed to provide a secure, agent-friendly, and self-describing interface for core content operations.

Module 3: Stateless Token Authentication  
This module implements a secure, stateless authentication mechanism for the AI agent. It uses JSON Web Tokens (JWT) sent as a Bearer Token, which is a standard for securing REST APIs. This approach ensures that every request is individually authenticated without relying on server-side sessions.    

Technical Tasks  
Integrate a PHP JWT Library: Install a robust JWT library like firebase/php-jwt via Composer to handle token encoding and decoding.    

Create a Token Issuance Endpoint: Implement a new REST API endpoint at /ascension/v1/token. This endpoint will accept a user's WordPress username and password. Upon successful validation using the core wp\_authenticate() function, it will generate and return a signed JWT.    

Implement Request Authentication Hook: Hook into WordPress's rest\_api\_init action. This hook will inspect the Authorization header of every incoming request to the /ascension/v1/ namespace.

Develop Token Validation Logic: The hooked function will parse the Bearer \<token\> from the header. It will use the JWT library to decode and verify the token's signature and expiration. If the token is valid, the user ID within the token's payload will be used to set the current user for the request via wp\_set\_current\_user(). If the token is invalid, expired, or missing, the request will be rejected with a 401 Unauthorized error.

API Contracts  
Endpoint: POST /ascension/v1/token

Description: Authenticates an agent using WordPress credentials and returns a JWT.

Request Body (JSON):

JSON

{  
  "username": "ai\_agent\_user",  
  "password": "agent\_application\_password"  
}  
Success Response (200 OK):

JSON

{  
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",  
  "token\_type": "Bearer",  
  "expires\_in": 3600  
}  
Error Response (401 Unauthorized):

JSON

{  
  "code": "invalid\_credentials",  
  "message": "Invalid username or password."  
}  
Authenticated API Request

Description: Any request to a protected endpoint within the /ascension/v1/ namespace.

Header: Authorization: Bearer \<jwt\_token\>

Behavior:

If the token is valid, the request is processed with the permissions of the associated user.

If the token is invalid, expired, or missing, the API returns an error.

Error Response (401 Unauthorized):

JSON

{  
  "code": "jwt\_auth\_invalid\_token",  
  "message": "Invalid authentication token.",  
  "data": {  
    "status": 401  
  }  
}  
Module 4: Atomic Content Primitives  
This module provides a minimal set of single-purpose, "atomic" API endpoints for content manipulation. This design is crucial for AI agents, as it breaks down complex operations into a sequence of simple, predictable steps, reducing cognitive load and the likelihood of errors.    

Technical Tasks  
Register Custom REST Routes: Use the register\_rest\_route function to define the following endpoints within the /ascension/v1/ namespace.

Implement Create Logic: The POST /nodes callback will use wp\_insert\_post() to create a new post. It will enforce a default post\_status of draft to ensure content is not published accidentally.

Implement Update Logic: The PATCH /nodes/{id} callback will use wp\_update\_post() to modify the post\_title and post\_content of an existing post. It will perform a capability check (e.g., current\_user\_can('edit\_post', $id)) to ensure the authenticated agent has permission.

Implement Read Logic: The GET /nodes/{id} callback will use get\_post() to retrieve a post's data and will also perform a capability check (e.g., current\_user\_can('read\_post', $id)).

API Contracts  
Endpoint: POST /ascension/v1/nodes

Method: POST

Description: Creates a new content node in a draft state.

Request Body (JSON):

JSON

{  
  "title": "New Post Title",  
  "content": "Plain text content for the new post."  
}  
Success Response (201 Created):

Headers: Location: /ascension/v1/nodes/{new\_post\_id}

Body: The full JSON object of the newly created node.

Endpoint: PATCH /ascension/v1/nodes/{id}

Method: PATCH

Description: Updates the title or content of an existing node.

Request Body (JSON):

JSON

{  
  "title": "Updated Post Title",  
  "content": "Updated plain text content."  
}  
Success Response (200 OK): The full JSON object of the updated node.

Error Response (404 Not Found): If no node with the specified {id} exists.

Module 5: Simplified Semantic Affordances  
This module enhances the API by embedding hypermedia controls directly into responses. This practice, a core tenet of HATEOAS (Hypermedia as the Engine of Application State), makes the API self-describing, allowing the AI agent to discover possible actions dynamically rather than relying on hardcoded logic.    

Technical Tasks  
Modify the GET /nodes/{id} Response: Filter the response of the single node endpoint to inject a \_links object.

Implement State-Based Logic: The logic will check the post\_status of the retrieved node.

Dynamically Generate Links: Based on the node's status, generate a list of valid actions (affordances). For the MVP, a node in draft status should present links for updating itself and for requesting publication. A published node would present different actions. This makes the API "explorable" for the agent.    

API Contract  
Endpoint: GET /ascension/v1/nodes/{id}

Method: GET

Description: Retrieves a single content node, including a list of permissible next actions based on its current state.

Example Success Response (for a draft node):

JSON

{  
  "id": 123,  
  "status": "draft",  
  "title": "My Draft Post",  
  "content": "Some draft content.",  
  "\_links": {  
    "self": {  
      "href": "/ascension/v1/nodes/123",  
      "method": "GET"  
    },  
    "update": {  
      "href": "/ascension/v1/nodes/123",  
      "method": "PATCH",  
      "description": "Update the title or content of this draft."  
    },  
    "request\_publication": {  
      "href": "/ascension/v1/governance/approval\_requests",  
      "method": "POST",  
      "description": "Submit this node for human review before publication."  
    }  
  }  
}  
Example Success Response (for a publish node):

JSON

{  
  "id": 124,  
  "status": "publish",  
  "title": "My Published Post",  
  "content": "Some published content.",  
  "\_links": {  
    "self": {  
      "href": "/ascension/v1/nodes/124",  
      "method": "GET"  
    },  
    "unpublish": {  
      "href": "/ascension/v1/nodes/124/unpublish",  
      "method": "POST",  
      "description": "Revert this node to a draft state."  
    }  
  }  
}

Here are the technical specifications for the final Traceability Modules of the WordPress Ascension MVP. These modules are designed to ensure every AI-driven action is auditable and that a robust human oversight process is programmatically enforced for critical operations.

Module 6: Programmatic Human-in-the-Loop (HITL) Endpoint  
This module establishes a formal, API-driven workflow for an AI agent to request human approval before executing sensitive or irreversible actions. This embeds human judgment directly into the automated process, making it a core feature rather than a manual override. This is a critical control mechanism to prevent errors and ensure accountability.   

Technical Tasks  
Create a Governance Database Table: A new table (e.g., ascension\_approval\_requests) will be created to store and track all approval requests. It will include columns for request\_id (primary key), agent\_user\_id, target\_resource\_id, requested\_action, status (e.g., 'pending', 'approved', 'rejected'), justification\_text, request\_timestamp, resolver\_user\_id, and resolution\_timestamp.

Register an Approval Request Endpoint: A new route will be created at POST /ascension/v1/governance/approval\_requests.

Implement Request Logic: The callback for this endpoint will:

Validate that the authenticated agent has permission to request the specified action.

Create a new record in the ascension\_approval\_requests table with a pending status.

Trigger an out-of-band notification (e.g., via a webhook or email) to human users with the required capabilities to approve the action (e.g., 'editor' role).

Return a 202 Accepted response to the agent, signaling that the request is queued. This programmatic pause is essential for agentic workflows.   

Register an Approval Resolution Endpoint: A separate, secure endpoint will be created at POST /ascension/v1/governance/approvals/{request\_id} for human operators to submit their decision.

Implement Resolution Logic: The callback for this endpoint will:

Verify that the authenticated human user has the necessary capabilities to approve the request.

Update the corresponding record in the ascension\_approval\_requests table with the decision ('approved' or 'rejected'), the resolver's user ID, and a timestamp.

If the decision is 'approved', the system will then execute the original requested action (e.g., publish the post).

API Contracts  
Endpoint: POST /ascension/v1/governance/approval\_requests

Description: Allows an AI agent to submit a high-stakes action for human review.

Request Body (JSON):

JSON

{  
  "action": "publish\_node",  
  "target\_resource\_id": 123,  
  "justification": "The AI-generated draft on 'Quantum Computing' is complete and meets all content guidelines."  
}  
Success Response (202 Accepted):

JSON

{  
  "request\_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",  
  "status": "pending",  
  "message": "Action has been queued for human approval. The workflow is paused pending review."  
}  
Error Response (403 Forbidden): If the agent attempts to request an action it is not permitted to perform.

Endpoint: POST /ascension/v1/governance/approvals/{request\_id}

Description: Allows an authorized human operator to approve or reject a pending request.

Request Body (JSON):

JSON

{  
  "decision": "approved",  
  "comments": "Looks good. Approved for immediate publication."  
}  
Success Response (200 OK):

JSON

{  
  "request\_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",  
  "status": "approved",  
  "message": "Approval processed. The 'publish\_node' action has been executed."  
}  
Error Response (403 Forbidden): If the user making the request does not have the capability to approve the action.

Module 7: Immutable Action Log  
This module provides a non-modifiable, append-only audit trail of every action taken by an authenticated agent. This creates a ground truth for all system interactions, which is essential for debugging, security analysis, and ensuring agent accountability.

Technical Tasks  
Create an Action Log Database Table: A new table (e.g., ascension\_action\_log) will be created with an append-only write pattern. It will store log\_id, timestamp, agent\_user\_id, source\_ip, endpoint\_called (e.g., 'POST /ascension/v1/nodes'), request\_payload, and response\_http\_status.

Implement a Logging Hook: A function will be attached to the rest\_api\_init action. This function will add a filter to rest\_pre\_dispatch that specifically targets the /ascension/v1/ namespace.

Develop Logging Logic: The filter's callback will execute after the primary API endpoint logic has completed. It will capture the details of the request (authenticated user, endpoint, payload) and the resulting HTTP status code of the response.

Write to Log: The captured data will be written as a new, immutable entry into the ascension\_action\_log table. The logging operation will be designed to fail silently (e.g., log to a file as a fallback) to ensure that a logging failure does not interrupt the primary API response to the agent.

API Contract (System Behavior)  
This module is an internal system function and does not expose a direct API endpoint for external interaction. Its behavior is defined by its response to other API calls.

Trigger: Any authenticated API call made to any endpoint within the /ascension/v1/ namespace.

Behavior: The system automatically records a detailed, timestamped entry of the transaction to the immutable log table after the request is processed and a response is sent to the agent. This process is non-blocking and invisible to the calling agent.

Data Logged:

Timestamp: The exact time of the API request.

Agent ID: The WordPress user ID of the authenticated AI agent.

Source IP: The IP address from which the request originated.

Endpoint Called: The specific API endpoint and method (e.g., PATCH /ascension/v1/nodes/123).

Request Payload: A serialized JSON string of the request body.

Response Status: The final HTTP status code returned to the agent (e.g., 201, 400, 404).

Sources and related content

Here is a recommended file and directory structure for a custom WordPress plugin that would house all the modules and API endpoints for the WordPress Ascension MVP.

This structure is designed to be modular, scalable, and follow modern WordPress development best practices, including the use of Composer for managing third-party libraries like the JWT package.  

/wp-ascension-mvp/  
|  
├── wp-ascension-mvp.php            \# Main plugin file: handles initialization, activation/deactivation hooks.  
|  
├── composer.json                   \# Defines PHP dependencies (e.g., firebase/php-jwt).  
|  
├── readme.txt                      \# Standard WordPress plugin readme file.  
|  
├── vendor/                         \# Managed by Composer for third-party libraries.  
│   ├── autoload.php  
│   └── firebase/  
│       └── php-jwt/  
|  
└── includes/                       \# Core plugin logic and modules.  
|  
    ├── core/                       \# Core setup and sandboxing.  
    │   ├── class-plugin-loader.php \# Main class to load all modules and register hooks.  
    │   ├── class-database-manager.php \# Handles creation of custom tables on activation (for HITL & logs).  
    │   └── class-sandboxing.php    \# Implements "Presentation Layer Retirement".  
|  
    ├── api/                        \# All REST API related functionality.  
    │   ├── class-api-registrar.php \# Registers all custom API routes and endpoints.  
    │   │  
    │   ├── endpoints/              \# Classes for each specific API endpoint.  
    │   │   ├── class-auth-endpoint.php       \# Handles JWT token issuance (/token).  
    │   │   ├── class-content-endpoint.php    \# Handles atomic content primitives and affordances (/nodes).  
    │   │   └── class-governance-endpoint.php \# Handles HITL approval requests (/governance).  
    │   │  
    │   └── middleware/             \# Middleware for API requests.  
    │       └── class-auth-middleware.php \# Validates JWT on incoming API requests.  
    │  
    └── traceability/               \# Traceability and logging modules.  
        └── class-action-logger.php   \# Implements the "Immutable Action Log".

### **Explanation of Key Files and Directories:**

* **`wp-ascension-mvp.php` (Main Plugin File):**  
  * This is the entry point of the plugin. It contains the plugin header comments that WordPress reads to display plugin information in the admin panel.    
  * It's responsible for including the Composer autoloader and initializing the main `Plugin_Loader` class.  
  * It will also contain the plugin activation and deactivation hooks, which will trigger the `Database_Manager` to create or remove the custom tables for logging and governance.  
* **`composer.json`:**  
  * This file manages the project's PHP dependencies. For this MVP, its primary role is to require the `firebase/php-jwt` library, which will be used for stateless token authentication.  
* **`vendor/`:**  
  * This directory is automatically generated and managed by Composer. It contains the actual files for third-party libraries like `php-jwt` and the autoloader script that makes their classes available to the plugin.  
* **`includes/core/`:**  
  * **`class-plugin-loader.php`:** A central controller that instantiates all other classes and registers their methods with the appropriate WordPress action and filter hooks (e.g., `add_action('rest_api_init',...)`).    
  * **`class-database-manager.php`:** Contains the SQL and logic to create the `ascension_approval_requests` and `ascension_action_log` tables upon plugin activation. This isolates database schema management.    
  * **`class-sandboxing.php`:** This class houses the **Presentation Layer Retirement** module. It will contain the method hooked into `template_redirect` to intercept all frontend requests and return a `404`.  
* **`includes/api/`:**  
  * **`class-api-registrar.php`:** This class is hooked into `rest_api_init`. Its job is to call `register_rest_route()` for all the custom endpoints (`/token`, `/nodes`, `/governance`), delegating the callback logic to the respective endpoint classes.    
  * **`endpoints/`:** This directory keeps the logic for each API resource separate and organized.  
    * `class-auth-endpoint.php`: Implements the **Stateless Token Authentication** logic for issuing JWTs.  
    * `class-content-endpoint.php`: Implements the **Atomic Content Primitives** for creating, reading, and updating nodes. It also contains the validation logic for the **Simplified Content Model** and the logic to add **Simplified Semantic Affordances** to responses.  
    * `class-governance-endpoint.php`: Implements the **Programmatic HITL Endpoint** for creating and resolving approval requests.  
  * **`middleware/class-auth-middleware.php`:** Contains the logic used in the `permission_callback` for protected endpoints. It checks for a valid Bearer token in the `Authorization` header and verifies it, ensuring secure access.  
* **`includes/traceability/`:**  
  * **`class-action-logger.php`:** Implements the **Immutable Action Log**. This class hooks into the REST API request lifecycle to capture every agent action and save it to the custom log table, ensuring a complete audit trail.

