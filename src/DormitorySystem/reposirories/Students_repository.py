from src.DormitorySystem.database.database import get_connection


def create(author_id: int, book_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO author_books(author_id, book_id)
        VALUES (?, ?)
    """, (author_id, book_id))

    conn.commit()
    conn.close()


def get_authors_by_book(book_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT a.author_id, a.name, a.surname, a.patronymic
        FROM author_books ab
        JOIN authors a ON ab.author_id = a.author_id
        WHERE ab.book_id = ?
    """, (book_id,))

    rows = cur.fetchall()
    conn.close()

    return rows


def get_books_by_author(author_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT b.book_id, b.name, b.isbn
        FROM author_books ab
        JOIN books b ON ab.book_id = b.book_id
        WHERE ab.author_id = ?
    """, (author_id,))

    rows = cur.fetchall()
    conn.close()

    return rows


def delete_by_book(book_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM author_books
        WHERE book_id = ?
    """, (book_id,))

    conn.commit()
    conn.close()