using UnityEngine;
using System.Collections;

public class PlayerController : MonoBehaviour {

    public float moveForce;
    public float maxSpeed;
    public float jumpForce;
    [HideInInspector]public bool facingRight = true;

    private Rigidbody2D rb2d;
    private Animator animCont;
    private Transform groundCheck;
    private bool grounded = false;
    private bool jump = false;


	// Use this for initialization
	void Start()
    {
        rb2d = GetComponent<Rigidbody2D>();
        animCont = GetComponent<Animator>();
        groundCheck = transform.Find("grounded");
	}
	
	// Update is called once per frame
	void Update()
    {
        grounded = Physics2D.Linecast(transform.position, groundCheck.position, 1 << LayerMask.NameToLayer("Ground"));
        if (Input.GetButtonDown("Jump") && grounded)
        {
            jump = true;
            Debug.Log("Attempt to Jump");
            grounded = false;
        }
	}

    void FixedUpdate()
    {
        float h = Input.GetAxis("Horizontal");

        animCont.SetFloat("Speed", Mathf.Abs(h));

        if (h == 0 && grounded)
            rb2d.velocity = new Vector2(0, rb2d.velocity.y);

        if (h * rb2d.velocity.x < maxSpeed)
            rb2d.AddForce(Vector2.right * h * moveForce);

        if (Mathf.Abs(rb2d.velocity.x) > maxSpeed)
            rb2d.velocity = new Vector2 (Mathf.Sign(rb2d.velocity.x) * maxSpeed, rb2d.velocity.y);
        
        if (h < 0 && facingRight)
            Flip();
        else if (h > 0 && !facingRight)
            Flip();

        if (jump)
        {
            jump = false;
            //animCont.SetTrigger("Jump");
            rb2d.velocity = new Vector2(rb2d.velocity.x, jumpForce);
        }


    }

    void Flip()
    {
        facingRight = !facingRight;

        float xScale = transform.localScale.x;
        transform.localScale = new Vector3(xScale * -1, transform.localScale.y, transform.localScale.z); 
    }
}
